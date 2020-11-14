from gpiozero import Button
from signal import pause
from subprocess import check_call

def red_pressed():
    print("red pressed")

def red_released():
    print("red released")

def red_held():
    print("shutdown")
    check_call(['sudo', 'poweroff'])

def green_pressed():
    print("green pressed")

def green_released():
    print("green released")

red_button = Button(23, hold_time=3)
red_button.when_pressed = red_pressed
red_button.when_released = red_released
red_button.when_held = red_held

green_button = Button(3)
green_button.when_pressed = green_pressed
green_button.when_released = green_released


pause()