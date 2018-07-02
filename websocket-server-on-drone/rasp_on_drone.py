import RPi.GPIO as GPIO
import time
       

def open_dump(duration=10, channel=26):
    GPIO.setmode(GPIO.BCM)
    time.sleep(1)
    GPIO.setup(channel, GPIO.OUT)
    #GPIO.output(channel, GPIO.LOW)
    #time.sleep(5)
    GPIO.output(channel, GPIO.HIGH) 
    #time.sleep(0.5)
    #GPIO.output(channel, GPIO.LOW)
    time.sleep(duration)
    GPIO.cleanup()

if __name__ == "__main__":
    channel = 26
    open_dump(channel)
