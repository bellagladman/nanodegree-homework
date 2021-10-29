"""
TASK 3 (Testing)

Question 1
Use the Simple ATM program to write unit tests for your functions.
You are allowed to re-factor your function to ‘untangle’ some logic
into smaller blocks of code to make it easier to write tests.
Try to write at least 5 unit tests in total covering various cases.
"""

import unittest
from task_2_atm_program import set_correct_pin, check_pin_is_correct, set_account_balance, request_withdrawal, update_account_balance, make_a_withdrawal


class TestMakeAWithdrawal(unittest.TestCase):
    def test_set_correct_pin(self):
        self.assertEqual(set_correct_pin(1234), 1234)
        self.assertEqual(set_correct_pin(1990), 1990)
        self.assertEqual(set_correct_pin(3456), 3456)
        self.assertRaises(ValueError, set_correct_pin, 12345)
        self.assertRaises(ValueError, set_correct_pin, "hello")

    def test_set_account_balance(self):
        self.assertEqual(set_account_balance(100), 100)
        self.assertRaises(ValueError, set_account_balance, -50)

    def test_update_account_balance(self):
        self.assertEqual(update_account_balance(account_balance=100, withdrawal_request=50), 50)

        # with self.assertRaises(ValueError):
        #     update_account_balance(-100, 50)
        # this could be useful IF I could get it to work with the values fed in by other functions

    # def test_check_pin_is_correct(self):
        # I am unsure how to check a for loop with a self.assert statement

    # def test_request_withdrawal(self):
        # I have already written assert statements in the function itself
        # I can't test those assert statements with a unittest because they refer to a local variable withdrawal_request
        # Unsure if this is something I would/should do, anyway? Are assert statements enough?

    # def test_make_a_withdrawal(self):
        # Because this function makes use of returned values from all the other functions,
        # I'm not entirely sure how you can unit test this!


if __name__ == '__main__':
    unittest.main()
