import unittest
from randomgame import validate_guess, check_guess # the source code functions to test

class GuessTest(unittest.TestCase):
    def test_validation_proper(self):
        guess = 12
        ulimit = 10
        llimit = 1
        self.assertEqual(False, validate_guess(guess, llimit, ulimit))
    def test_validation_string(self):
        guess = 'haha'
        ulimit = 10
        llimit = 1
        self.assertEqual(False, validate_guess(guess, llimit, ulimit))
    def test_input_right_guess(self):
        answer = 5
        guess = 5
        self.assertEqual('correct', check_guess(guess, answer))
    def test_input_wrong_guess_low(self):
        answer = 5
        guess = 3
        self.assertEqual('low', check_guess(guess, answer))
    def test_input_wrong_guess_high(self):
        answer = 5
        guess = 9
        self.assertEqual('high', check_guess(guess, answer))

if __name__ == '__main__':
    unittest.main()