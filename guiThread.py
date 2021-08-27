import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from numpy import random
from threading import *
import time

# Button definitions
ID_START = wx.NewIdRef()
ID_STOP = wx.NewIdRef()

# Define notification event for thread completion
EVT_RESULT_ID = wx.NewIdRef()

def EVT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)

class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data

# Thread class that executes processing
class WorkerThread(Thread):
    """Worker Thread Class."""
    def __init__(self, notify_window):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self._notify_window = notify_window
        self._want_abort = 0
        # This starts the thread running on creation, but you could
        # also make the GUI thread responsible for calling this
        self.start()

    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread. Simulation of
        # a long process (well, 10s here) as a simple loop - you will
        # need to structure your processing so that you periodically
        # peek at the abort variable
        for i in range(20):
            time.sleep(1)
            if self._want_abort:
                # Use a result of None to acknowledge the abort (of
                # course you can use whatever you'd like or even
                # a separate event type)
                wx.PostEvent(self._notify_window, ResultEvent(None))
                return
            data = random.rand(20)
            print(f'Posting event {i}')
            wx.PostEvent(self._notify_window, ResultEvent(data))
        # Here's were the result would be returned (this is an
        # example fixed result of the number 10, but it could be
        # any Python object)
        wx.PostEvent(self._notify_window, ResultEvent(None))

    def abort(self):
        """abort worker thread."""
        # Method for use by main thread to signal an abort
        self._want_abort = 1


class MainFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title="Varactor Test Board", size=(1200, 580))
        self.save_path = r"C:\Users\emmas\data.csv"

        #Set up threading, worker thread will be the one doing measurements. OnResult is the result handler.
        EVT_RESULT(self, self.OnResult)
        self.worker = None


        # Add SplitterWindow panels
        self.split_win = wx.SplitterWindow(self)
        self.graph_panel = MatplotPanel(self.split_win)
        self.ctrl_menu = wx.Panel(self.split_win)
        self.split_win.SplitVertically(self.ctrl_menu, self.graph_panel, 200)

        #Define menu fields for voltage control.
        self.lvText = wx.StaticText(self.ctrl_menu, -1, 'Min Voltage (V)', size=(100,20), pos=(10,10))
        self.low_voltage = wx.TextCtrl(self.ctrl_menu, -1, 'Vlow', size=(80,20), pos=(10,30))
        #There need to be 3 of these: Vmin, Vmax, Vstep.

        #Select channel to tune.
        self.chText = wx.StaticText(self.ctrl_menu, -1, 'Tune Channel:', size = (100,20), pos = (10,200))
        self.chBox = wx.ComboBox(self.ctrl_menu,  choices =['1','2','3','4','5','6','7','8','Common'], size = (100,20), pos=(10,220))

        #Where do I save my data?
        self.flText=wx.StaticText(self.ctrl_menu, -1, 'Save File:', size=(100,20), pos=(10,250))
        self.file_path = wx.TextCtrl(self.ctrl_menu, -1, self.save_path, size=(180,20), pos=(10,270))

        #Add buttons. There should be a Start Sweep, Measure Single, and Save File
        self.measBut = wx.Button(self.ctrl_menu, -1, "Measure", size=(80, 40), pos=(10, 410))
        self.measBut.Bind(wx.EVT_BUTTON, self.measure)

        self.fileBut = wx.Button(self.ctrl_menu, -1, 'Save Location', size=(80,40), pos=(10,450))
        self.fileBut.Bind(wx.EVT_BUTTON, self.set_path)

        #Shorten calls to graph_panel figure and axes.
        self.fig = self.graph_panel.figure
        self.ax1 = self.graph_panel.axes

    def measure(self, event):
        self.measBut.SetBackgroundColour([0, 255, 0])
        self.measBut.SetLabel('Running')
        self.ax1.clear()
        self.ax1.set_title("Random Data")
        self.ax1.set_xlim([0,20])
        self.ax1.set_ylim([0,1])
        self.ax1.set_xlabel('Frequency (Hz)')
        self.ax1.set_ylabel('S11 (dB)')
        if not self.worker:
            self.worker = WorkerThread(self)

    def OnResult(self, event):
        if event.data is None:
            self.measBut.SetBackgroundColour('')
            self.measBut.SetLabel('Measure')
            self.worker = None
        else:
            print('preparing to plot')
            print(event.data)
            self.ax1.plot(range(20), event.data, 30)
            self.canvas = FigureCanvas(self.graph_panel, -1, self.fig)


    def set_path(self, event):

        fdlg = wx.FileDialog(self.ctrl_menu, "Select location to save data.", "", "", "CSV files(*.csv)|*.*", wx.FD_SAVE)

        if fdlg.ShowModal() == wx.ID_OK:
            self.save_path = fdlg.GetPath() + ".csv"
            self.file_path.SetValue(self.save_path)


class MatplotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size=(50, 50))

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        t = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        s = [0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 1.0, 2.0, 1.0, 0.0]

        self.axes.plot(t, s)
        self.canvas = FigureCanvas(self, -1, self.figure)

class MainApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp(0)
    app.MainLoop()