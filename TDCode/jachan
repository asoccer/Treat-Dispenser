import RPi.GPIO as GPIO
import time
import sys
Servo=19
Button=26
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Servo, GPIO.OUT)
p = GPIO.PWM(Servo, 50)
a=4
try:
  while True:  
    input_state = GPIO.input(Button)
    if input_state == False:
      print('Button Pressed')
      p.start(a)
      time.sleep(0.84)
      p.stop()
except KeyboardInterrupt:
  GPIO.cleanup()
====================
