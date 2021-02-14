from gpiozero import Button
from signal import pause
from subprocess import check_call
import player
import shared

def reset_last_code():
    shared.last_code = ""

def power_button_pressed():
    print("power pressed")
    player.stop()
    reset_last_code()

def power_button_released():
    print("power released")

def power_button_held():
    print("shutdown")
    player.play_mpd("shutdown.wav")
    check_call(['sudo', 'poweroff'])

def play_button_pressed():
    print("play pressed")
    player.toggle_pause()

def play_button_released():
    print("play released")

def play_button_held():
    print("play held")

def next_button_pressed():
    print("next pressed")
    player.next()
    reset_last_code()

def next_button_released():
    print("next released")

def next_button_held():
    print("next held")

def previous_button_pressed():
    print("previous pressed")
    player.previous()
    reset_last_code()

def previous_button_released():
    print("previous released")

def previous_button_held():
    print("previous held")


power_button = Button(23, hold_time=3)
power_button.when_pressed = power_button_pressed
power_button.when_released = power_button_released
power_button.when_held = power_button_held

play_button = Button(3, hold_time=3)
play_button.when_pressed = play_button_pressed
play_button.when_released = play_button_released
play_button.when_held = play_button_held

next_button = Button(7, hold_time=3)
next_button.when_pressed = next_button_pressed
next_button.when_released = next_button_released
next_button.when_held = next_button_held

previous_button = Button(25, hold_time=3)
previous_button.when_pressed = previous_button_pressed
previous_button.when_released = previous_button_released
previous_button.when_held = previous_button_held


# pause()
