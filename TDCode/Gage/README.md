
The set up of I2C audio on the Raspberry Pi Zero W with the "aplay" functionality is as follows.
1. Use AdaFruit MAX98357 I2C amplifier (Hardware)
2. The Pinout (for this code atleast) is using SetupMode BCM. This is different from Setupmode(BOARD) as the pins are different. 
3. Follow this link for easy set up: https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/raspberry-pi-wiring 
    The link above shows you everything you need to do. Please go by BCM pinouts though. This is the problem I originally had. 
4. Once everything is set up, test the audio using their audio test described in the link.
5. In order to set it up with a push button, use the following code
-------------------------------------------------
import os                               
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)                                                      # set up the board (NOT GPIO.BOARD)!!!!
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)                           # set pin 23 to Input
while True:
    if (GPIO.input(23) == False):               #when button is grounded:
        os.system('aplay /home/pi/DogClickSound.wav')   # play the wav file (will need to record click sound as wav and enter path here)
    time.sleep(0.1)
--------------------------------------------------
the os.system('aplay <insert path name to wave file>') is the command that will play audio through the set up i2c
Sources:
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/raspberry-pi-wiring
https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/circuitpython-code
https://www.raspberrypi.org/forums/viewtopic.php?t=178441
For difference in BOARD vs BCM:
https://www.raspberrypi.org/forums/viewtopic.php?t=34273
Click Sound adapted from:
