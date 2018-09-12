#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

red = [255, 0, 0]
blue = [0, 0, 255]

def draw_alarm():
    sense.clear(red)
    sleep(0.40)
    sense.clear(blue)
    sleep(0.40)
    sense.clear(red)
    sleep(0.40)
    sense.clear(blue)
    sleep(0.40)
    sense.clear(red)
    sleep(0.40)
    sense.clear(blue)
    sleep(0.40)
    sense.clear(red)
    sleep(0.40)
    sense.clear()

draw_alarm()
