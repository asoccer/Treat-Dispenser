import RPi.GPIO as GPIO
import time
import sys

# GLOBAL SETUP
# SET 7 AS OUTPUT
# This sets pin 7 as the signal, pin 2 will be for 5V input for the Servo, Pin 6 will be for GROUND

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Pin 10 will be the signal the button sends a high to.




#MAIN CODE LOOP FOR MANAGING THE DUTY CYCLE

def codeLoop(p):
    print("Button input has been received
    p.start(4)
    time.sleep(2)
    p.stop()
    
#INITIALIZATION PARAMETERS FOR SETTING PULSE WIDTH MODULE

def init():
  p = GPIO.PWM(7,50)
  return p

def main():
  p = init()
  GPIO.add_event_detect(10,GPIO.RISING,callback=codeLoop(p))
  while(1):
          print("No commands")
          
main()
