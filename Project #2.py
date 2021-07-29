import pylab
import csv


myData = []
with open('data_1.csv', newline='') as test:
    reader = csv.reader(test)
    print(reader)
    for row in reader:
    #print(row)
        myData.append(row)

x = []
y1 = []
y2 = []
y3 = []
for item in myData[5:]:
    x.append(float(item[0]))
    y1.append(float(item[1]))
    y2.append(float(item[2]))
    y3.append(float(item[3]))
pylab.plot(x,y1)
pylab.plot(x,y2)
pylab.plot(x,y3)
pylab.title('Output from Varactor Board')
pylab.xlabel('Time in Seconds')
pylab.ylabel('Volts')
pylab.savefig('my_picture.png')
pylab.show()
