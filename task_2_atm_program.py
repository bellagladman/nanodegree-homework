"""
TASK 2 (Exception Handling)
Question 1
Simple ATM program
Using exception handling code blocks such as try/ except / else / finally
(NB: the more the better, but try to use at least two key words e.g. try/except)

Write a program that simulates and ATM machine to withdraw money.
Tasks:
Prompt user for a pin code
If the pin code is correct then proceed to the next step,
otherwise ask a user to type in a password again.
You can give a user a maximum of 3 attempts and then exit a program.

Set account balance to 100.
Now we need to simulate cash withdrawal
Accept the withdrawal amount
Subtract the amount from the account balance and display the remaining balance
(NOTE! The balance cannot be negative!)
However, when a user asks to ‘withdraw’ more money than they have on their account,
then you need to raise an error and exit the program.

"""


# Set account balance
account_balance = 100

# Set correct PIN
correct_pin = 1234


def check_pin_is_correct():
    pin_entry = int(input('Please type in your PIN: '))
    count = 1
    if pin_entry == correct_pin:
        print("PIN entered successfully.")
        return True
    else:
        while pin_entry != correct_pin and count <= 2:
            print("Incorrect pin entered. Please try again.")
            pin_entry = int(input('Please type in your PIN: '))
            count += 1
            if pin_entry != correct_pin and count == 3:
                print("Incorrect PIN entered too many times. Please contact your bank.")
                return False
            elif pin_entry == correct_pin:
                print("PIN entered successfully.")
                return True


def withdraw_cash(balance):
    try:
        withdrawal_request = int(input('How much money would you like to withdraw? '))
        assert 0 <= withdrawal_request, "You can't withdraw a negative number. Please try again."
        assert withdrawal_request <= balance, "Insufficient funds. Please try again."
    except Exception as e:
        print(e)
    else:
        account_balance = balance - withdrawal_request
        print("Your request for £{:.2f} has been accepted. Please take your cash.".format(withdrawal_request))
        print("Your new account balance is: £{:.2f}.".format(account_balance))

def make_a_withdrawal():
    if check_pin_is_correct():
        withdraw_cash(account_balance)
    else:
        pass


if __name__ == '__main__':
    make_a_withdrawal()
