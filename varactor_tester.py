import time
import os
import logging
import matplotlib.pyplot as plt
import qcodes as qc
import pandas as pd
import numpy as np
from qcodes.dataset.experiment_container import new_experiment, load_experiment_by_name
from qcodes.dataset.measurements import Measurement
from qcodes.instrument_drivers.yokogawa import GS200
import qcodes.instrument_drivers.Keysight.N5245A as N5245A

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

exp_name = 'PNA_Test2'
sample_name = 'varactor_12V_3.2K_ch12only'
indPlot = False

pPower = -20
pStart = 160e6
pStop =380e6
pPoints = 5000

vmin = 0
vmax = 11
vstep = 1
vrange = np.arange(vmin, vmax, vstep)

try:
    exp = load_experiment_by_name(exp_name, sample=sample_name)
    print('Experiment loaded. Last ID no:', exp.last_counter)
except ValueError:
    exp = new_experiment(exp_name, sample_name)
    print('Starting new experiment.')

pna = N5245A.N5245A('PNA', 'GPIB0::16::INSTR')
dc = GS200.GS200('dc','GPIB0::1::INSTR')
dc.voltage_range(10)

os.mkdir(os.path.join(r"C:\Users\Michael\Downloads",sample_name))

plt.ion()
f, ax = plt.subplots(1,1, figsize = (9,6))
ax.set(xlabel = 'Frequency (Hz)', ylabel='Intensity (dB)', title = f'Data for {sample_name}')
mFigname = os.path.join(r"C:\Users\Michael\Downloads",sample_name, sample_name+'.png')


for vltg in vrange:
    vstr = str(vltg)
    fname = os.path.join(r"C:\Users\Michael\Downloads", sample_name, sample_name+'_voltage_'+vstr+'.csv')
    figname = os.path.join(r"C:\Users\Michael\Downloads", sample_name, sample_name+'_voltage_'+vstr+'.png')
    dc.voltage.set(vltg)
    dc.output('on')

    pna.power(pPower)
    pna.start(pStart)
    pna.stop(pStop)
    pna.points(pPoints)
    pna.trace("S11")

    # Enable 2 averages, and set IF BW to 1kHz
    pna.if_bandwidth(1e3)
    pna.averages_enabled(True)
    pna.averages(1)

    # Run a measurement
    meas = Measurement()
    meas.register_parameter(pna.magnitude)

    with meas.run() as datasaver:
        mag = pna.magnitude()
        datasaver.add_result((pna.magnitude, mag))
        dataid = datasaver.run_id
        dataset = datasaver.dataset

    plotMe = dataset.to_pandas_dataframe()

    ax.plot(plotMe, label = f"{vstr}V")
    ax.legend()
    plt.pause(0.2)
    plt.show()
    plt.savefig(mFigname)

    if indPlot:
        plt.plot(plotMe)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Intensity (dB)')
        plt.title(f'S11 for {sample_name} {vstr}V')
        plt.show(block = False)
        plt.savefig(figname)
        plt.pause(0.5)
        plt.close()

    plotMe.to_csv(fname)

dc.output('off')
