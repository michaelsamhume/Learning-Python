import qcodes as qc
from qcodes.instrument_drivers.tektronix.Keithley_2450 import Keithley2450
from qcodes.dataset import initialise_database, Measurement, new_experiment
from qcodes.dataset.plotting import plot_dataset
from visa import VisaIOError
import pylab
import csv

keithley = Keithley2450("keithley", "GPIB0::10::INSTR")
keithley.reset()
keithley.terminals("front")

keithley.source.function("voltage")
current = keithley.sense.function("current")
curList = []
voltList = []
volts=0
for x in range(40):
    volts += 0.05
    with keithley.output_enabled.set_to(True):
        keithley.source.voltage(volts)
        current = keithley.sense.current()
        curList.append(current)
        voltList.append(volts)
        print(f'Current is {current} for voltage {volts}')
        print(f"Approx. resistance: ", volts // current)

print(curList)
print(voltList)
pylab.title('Output from Keithley 2450 SourceMeter')
pylab.xlabel('Voltage')
pylab.ylabel('Current')
pylab.plot(curList)
pylab.show()




# keithley.source.function("current")
# keithley.source.current(1E-6)  # Put 1uA through the resistor
# current_setpoint = keithley.source.current()
# voltage = keithley.sense.function("voltage")
# with keithley.output_enabled.set_to(True):
#     voltage = keithley.sense.voltage()
#     me = input('foio')
# print(f"Approx. resistance: ", voltage // current_setpoint)

