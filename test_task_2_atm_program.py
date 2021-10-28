"""
TASK 3 (Testing)

Question 1
Use the Simple ATM program to write unit tests for your functions.
You are allowed to re-factor your function to ‘untangle’ some logic
into smaller blocks of code to make it easier to write tests.
Try to write at least 5 unit tests in total covering various cases.
"""

import unittest
from task_2_atm_program import check_pin_is_correct, withdraw_cash, make_a_withdrawal

class TestMakeAWithdrawal(unittest.TestCase):
    def test_values(self):
        # Make sure error is raised when withdrawal_request is a negative number
        self.assertRaises(ValueError, withdraw_cash(balance), -2)
