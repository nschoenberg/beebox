
import json
from collections import namedtuple
from enum import Enum

InterpreterResult = namedtuple("InterpreterResult", "action arg")
Action = Enum("Action", "none play play_mpd text2speech terminate")

EXIT_CODE = "0011043608"


def interpret(code):
    if (not code):
        return InterpreterResult(Action.none, "")

    print("Startint to interpret code:" + code)
    card = get_card_binding(code)

    if (code == EXIT_CODE):
        result = InterpreterResult(Action.terminate, "")
    elif (code == "0010455958"):
        result = InterpreterResult(Action.play, "test.wav")
    elif (card != "None"):
        action = Action.play_mpd
        if (card["kind"] in Action.__members__):
            action = Action[card["kind"]]

        result = InterpreterResult(action, card)
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
