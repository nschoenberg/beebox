# Dependencies
- Python 3.9
- python-pip
- python-evdev
- Aplay (command line sound)
- mpd / mpc
- pip3 install python-mpd2

# Hardware
- pi zero w
- hifiberry mini amp


# gpio
GPIOs 18-21 (pins 12, 35, 38 and 40) are used for the sound interface. GPIO16 can be used to mute the power stage. GPIO26 shuts down the power stage. You can’t use these GPIOs for any other purpose.

Source: https://www.hifiberry.com/docs/hardware/gpio-usage-of-hifiberry-boards/