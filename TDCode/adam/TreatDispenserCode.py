import RPi.GPIO as GPIO
import time
import sys

# GLOBAL SETUP
# SET 7 AS OUTPUT
# This sets pin 7 as the signal, pin 2 will be for 5V input for the Servo, Pin 6 will be for GROUND

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)


#MAIN CODE LOOP FOR MANAGING THE DUTY CYCLE

def codeLoop(p):
  try:
      while True:
          p.ChangeDutyCycle(4)
          time.sleep(2)
          sys.exit(0)
  except KeyboardInterrupt:
      GPIO.cleanup()
    
#INITIALIZATION PARAMETERS FOR SETTING PULSE WIDTH MODULE

def init():
  p = GPIO.PWM(7,50)
  return p

def main():
  p = init()
  codeLoop(p)
