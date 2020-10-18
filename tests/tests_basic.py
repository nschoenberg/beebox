import unittest
from beebox import interpreter

class TestStringMethods(unittest.TestCase):

    def test_interpret(self):
        result = interpreter.interpret("test")
        self.assertEqual(result.action, interpreter.CodeAction.play)
        self.assertEqual(result.arg, "test.wav")

if __name__ == '__main__':
    unittest.main()