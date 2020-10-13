# Intention of this script is to receive defaul keboard input from an rfid reader so that
# bound commands gets translated to actions

import sys
import evdev
from evdev import InputDevice, categorize, ecodes

scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 100: u'RALT'
}

code_buffer = []
code = ""
current_key = ""

def read():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    dev = InputDevice(devices[0].path)

    code_buffer.clear()
    current_key = ""

    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            current_key = ecodes.KEY[event.code]
            
            if event.value == 1: # handle only key down events 
                if current_key == "KEY_ENTER":
                    break
                else:
                    code_buffer.append(scancodes[event.code])
    
    code = "".join(code_buffer)
    dev.close()
    return code

if __name__ == '__main__':
    code = read()
    print(code)