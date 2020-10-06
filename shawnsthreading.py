from threading import Thread
import RPi.GPIO as GPIO
from time import sleep

class Actuator1:
    def __init__(self):
        self.stopped = False
        self.GPON = False

    def start(self, outPin, timing):
        t = Thread(target=self.run, args=(self, outPin, timing))
        t.daemon = True
        t.start()

    def run(self, outPin, timing):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(outPin, GPIO.OUT)
        while(True):
            if(self.stopped):
                GPIO.output(outPin, False)
                return
            GPIO.output(outPin, self.GPON)
            sleep(timing)
            self.GPON = not self.GPON
    
    def stop(self):
        self.stopped = True

class Actuator2:
    def __init__(self):
        self.stopped = False
        self.GPON = False

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        while(True):
            if(self.stopped):
                GPIO.output(24, False)
                return
            GPIO.output(24, self.GPON)
            sleep(0.5)
            self.GPON = not self.GPON
    
    def stop(self):
        self.stopped = True

class Actuator3:
    def __init__(self):
        self.stopped = False
        self.GPON = False

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)
        while(True):
            if(self.stopped):
                GPIO.output(25, False)
                return
            GPIO.output(25, self.GPON)
            sleep(0.7)
            self.GPON = not self.GPON
    
    def stop(self):
        self.stopped = True


greenLight = Actuator1(23, 0.5)
yellowLight = Actuator1(24, 0.5)
redLight = Actuator1(25, 0.7)

def main():
    greenLight.start()
    yellowLight.start()
    redLight.start()
    stopTimer = 20
    while(stopTimer > 0):
        stopTimer = stopTimer - 1
        sleep(1)
    greenLight.stop()
    yellowLight.stop()
    redLight.stop()
    exit()

if __name__ == "__main__":
    main()





    