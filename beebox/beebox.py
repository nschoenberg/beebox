# This is the main script of the program
import keyboard_input_handler
import interpreter
import player

code = ""

while True:
    # Read rfid code or manual input
    code = keyboard_input_handler.read()
    print(code)
    interpreted = interpreter.interpret(code)
    
    if (interpreted.action == interpreter.Action.play):
        player.play(interpreted.arg)
    if (interpreted.action == interpreter.Action.play_mpd):
        card = interpreted.arg
        print(card)
        player.play_mpd(card['uri'], card['index'], card['is_playlist'])
    elif (interpreted.action == interpreter.Action.terminate):
        break