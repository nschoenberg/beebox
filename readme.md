![Hardware](https://raw.githubusercontent.com/nschoenberg/beebox/master/box.jpg)

# Dependencies
- Python 3.9
- python3-pip
- python3-evdev
- Aplay (command line sound, used for startup sound)
- mpd / mpc
- pip3 install python-mpd2 (Also do sudo -H pip3 install python-mpd2 if you want to use launcher.sh)
- sudo apt-get install python3-gpiozero

# Configuration
launcher requires an alias to change into the root directory of the script
alias cdbeebox='cd /home/pi/share/beebox/'

# Hardware
- pi zero w
- hifiberry mini amp


# GPIO
GPIOs 18-21 (pins 12, 35, 38 and 40) are used for the sound interface. GPIO16 can be used to mute the power stage. GPIO26 shuts down the power stage. You can’t use these GPIOs for any other purpose.

Source: https://www.hifiberry.com/docs/hardware/gpio-usage-of-hifiberry-boards/

# Button Controller
GPIO 3 (PIN 5) + Ground PIN 6 is used by the play button. When the system is in halt mode, this button wakes up the system.

GPIO 23 (PIN 16) + Ground PIN 14 is used by the power button.

GPIO 25 (PIN 22) + Ground PIN 20 is used for the next button.

GPIO 7 (PIN 26) + Ground PIN 25 is used for the previous button.

# Pictures 
![Hardware](https://raw.githubusercontent.com/nschoenberg/beebox/master/hardware.png)

![GPIO](https://raw.githubusercontent.com/nschoenberg/beebox/master/hifiberrymini_gpio_cheatsheet.png)
