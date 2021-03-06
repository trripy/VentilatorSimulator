from threading import Thread
import random
import time
import matplotlib.pyplot as plt
import numpy as np
class Sensor1(Thread):
    def __init__(self,DataFrequency=0.05,freq=12,sensorError=4):
        Thread.__init__(self)
        self.DataFrequency=DataFrequency
        self.SensorReading=0 #default sensor reading
        # self.SensorError=sensorError # Standard deviation of the sensor.
        Fs = 1000
        f = freq
        sample = 1000
        x = np.arange(sample)
        self.i=0
        noise = 0.0008 * np.asarray(random.sample(range(0, 1000), sample))
        self.y = np.sin(2 * np.pi * f * x / Fs) + noise
        # plt.plot(x, self.y)
        # plt.xlabel('Time')
        # plt.ylabel('Respiratory sensor Value')
        # plt.show()
    def run(self):
        while 1:
            if self.i>=1000:
                self.i=0
            print(self.y[self.i])
            self.i+=1
            time.sleep(0.1)


# 'Sensor 1 Test'
sens1=Sensor1(4)
sens1.setName("Sensor 1")
sens1.start()

