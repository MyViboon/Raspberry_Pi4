import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO4 --> 4
GPIO.setwarnings(False)

relay = 4
GPIO.setup(relay, GPIO.OUT)

def TurnOn(sleep=2):
    GPIO.output(relay, False)
    if sleep > 0:
        time.sleep(sleep)
        
def TurnOff(sleep=2):
    GPIO.output(relay, True)
    if sleep > 0:
        time.sleep(sleep)       

while True:
    TurnOn(3)
    TurnOff(3)