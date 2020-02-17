
import os                               
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)                                                      # set up the board (NOT GPIO.BOARD)!!!!
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)                           # set pin 23 to Input
while True:
    if (GPIO.input(23) == False):               #when button is grounded:
        os.system('aplay /home/pi/DogClickSound.wav')   # play the wav file (will need to record click sound as wav and enter path here)
    time.sleep(0.1)
