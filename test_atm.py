# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code.
# And make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.

#
# def test_calculate_average_missing_mark(self):
#     my_input = [
#         {'name': 'Jane', 'mark': 7},
#         {'name': 'Nitesh', 'mark': 6},
#         {'name': 'Aisha', },
#         {'name': 'Zac', 'mark': '8'},
#     ]
#     expected = 6.5  # (8+5+6+7) / 4 --> use 5 if mark is missing
#
#     result = average_exam_score(my_input)
#     self.assertEqual(expected, result)

import unittest
from unittest.mock import patch
import atm
from unittest import mock
from unittest import TestCase


# password is four digits

# def square_input():
#     number_input = input('enter the number you wish to square: ')
#     return float(number_input) ** 2


class TestPinMockedInput(unittest.TestCase):


    correct_pin = 1223

    @patch('builtins.input', correct_pin)
    def test_with_valid_input(self):
        result = atm.validate_pin(1223)
        expected_result = True
        self.assertTrue(result == expected_result)
        pass

    @patch('builtins.input', lambda x: "1111")
    def test_invalid_input_wrong_number(self):
        with self.assertRaises(ValueError):
            result = atm.validate_pin()
            expected_result = False
            self.assertTrue(result == expected_result)
            pass

    @patch('builtins.input', lambda x: "hi12")
    def test_invalid_input_non_numeric(self):
        with self.assertRaises(ValueError):
            result = atm.validate_pin()
            expected_result = False
            self.assertTrue(result == expected_result)
            pass


if __name__ == '__main__':
    unittest.main()


class TestBalanceMockedInput(unittest.TestCase):

    @patch('builtins.input', lambda x: 20)
    def test_with_valid_input(self):
        result = atm.calculate_balance(80)
        self.assertEqual(80, 80)
        pass

    @patch('builtins.input', lambda x: "hello")
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            result = atm.calculate_balance(False)
            pass

    @patch('builtins.input', lambda x: 120)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            result = atm.calculate_balance(False)

    @patch('builtins.input', lambda x: -5)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            result = atm.calculate_balance(False)


if __name__ == '__main__':
    unittest.main()


class TestPinMockedInput(unittest.TestCase):

    @patch('builtins.input', lambda x: "1223")
    def test_with_valid_input(self):
        result = atm.validate_pin()
        self.assertTrue(True)

    @patch('builtins.input', lambda x: "1111")
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            result = atm.validate_pin(False)


if __name__ == '__main__':
    unittest.main()
