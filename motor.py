import RPi.GPIO as GPIO
from time import sleep 

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

while True: 
 GPIO.output(7, GPIO.HIGH) # Turn on
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(2) # Sleep for 2 second
 GPIO.output(7, GPIO.LOW) # Turn off
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(2) # Sleep for 2 second
