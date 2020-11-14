from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

def shutdown():
    print("shutdown")

button = Button(23, hold_time=5)

button.when_pressed = say_hello
button.when_released = say_goodbye
button.when_held = shutdown

pause()