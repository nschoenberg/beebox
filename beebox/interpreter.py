
from collections import namedtuple
from enum import Enum

InterpreterResult = namedtuple("InterpreterResult", "action arg")
Action = Enum("Action", "none play terminate")

EXIT_CODE = "0011043608"

def interpret(code):
    print("Startint to interpret code:" + code)
    
    if (code == EXIT_CODE):
        result = InterpreterResult(Action.terminate, "")
    elif (code == "0010455958"):
        result = InterpreterResult(Action.play, "test.wav")
    else:
        result = InterpreterResult(Action.play, code + ".wav")
    
    return result