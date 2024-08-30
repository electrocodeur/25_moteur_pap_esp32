import Stepper
from machine import Pin
import time

# for ESP32
In1 = Pin(32,Pin.OUT)
In2 = Pin(33,Pin.OUT)
In3 = Pin(25,Pin.OUT)
In4 = Pin(26,Pin.OUT)
s1 = Stepper.create(In1,In2,In3,In4, delay=1)
while True:
    s1.step(509) # faire tourner le moteur pas a pas dans le sens antihoraire
    time.sleep(1)
    s1.step(509,-1) # faire tourner le moteur pas a pas dans le sens horaire
    time.sleep(1)
