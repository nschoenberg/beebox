# This is the main script of the program
import keyboard_input_handler
import interpreter
import player
import speek
import button_controller

code = ""

while True:
    # Read rfid code or manual input
    if (keyboard_input_handler.can_read()):
        code = keyboard_input_handler.read()
        print(code)
    
    interpreted = interpreter.interpret(code)
    
    if (interpreted.action == interpreter.Action.play):
        player.play(interpreted.arg)
    if (interpreted.action == interpreter.Action.play_mpd):
        card = interpreted.arg
        print(card)
        player.play_mpd(card["uri"], card["index"], card["kind"] == "playlist")
    elif (interpreted.action == interpreter.Action.text2speech):
        card = interpreted.arg
        print("Speek to file:")
        print(card)
        speek.to_file(card["desc"])
        player.play_mpd(card["uri"])
    elif (interpreted.action == interpreter.Action.terminate):
        break