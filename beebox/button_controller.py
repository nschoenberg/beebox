from gpiozero import Button
from signal import pause
from subprocess import check_call

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

def shutdown():
    print("shutdown")
    check_call(['sudo', 'poweroff'])

button = Button(23, hold_time=3)

button.when_pressed = say_hello
button.when_released = say_goodbye
button.when_held = shutdown

pause()