
import json
from collections import namedtuple
from enum import Enum

InterpreterResult = namedtuple("InterpreterResult", "action arg")
Action = Enum("Action", "none play play_mpd terminate")

EXIT_CODE = "0011043608"

def interpret(code):
    print("Startint to interpret code:" + code)
    card = get_card_binding(code)

    if (code == EXIT_CODE):
        result = InterpreterResult(Action.terminate, "")
    elif (code == "0010455958"):
        result = InterpreterResult(Action.play, "test.wav")
    elif (card != "None"): #Bibi
        result = InterpreterResult(Action.play_mpd, card)
#0005370535 # Radio Hamburg
#0003847812 # Radio Teddy
#0010397350 # Radio Teddy Gn8 Stories

    else:
        result = InterpreterResult(Action.play, code + ".wav")
    
    return result

def get_card_binding(cardId):
    bindings = get_card_bindings()
    if cardId in bindings:
        card = bindings[cardId]
        return card

def get_card_bindings():
    with open("./beebox/card_bindings.json") as f:
        data = json.load(f)
        return data

