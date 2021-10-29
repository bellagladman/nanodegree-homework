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


# Set correct PIN
def set_correct_pin(pin):
    if not isinstance(pin, int):
        raise ValueError("PINs must be a four digit number.")
    if not 1000 <= pin < 9999:  # I have not been able to figure out a way to allow PINs to start with 0
        raise ValueError("PINs must be four digits")
    else:
        correct_pin = pin
    # print('Correct pin set to: {}'.format(correct_pin))
    return correct_pin


def check_pin_is_correct(correct_pin):
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


# Set account balance
def set_account_balance(balance):
    if balance < 0:
        raise ValueError("You can't add negative money to your bank account.")
    else:
        account_balance = balance
    # print("Your account balance is: {}".format(account_balance))
    return account_balance


def request_withdrawal(account_balance):
    try:
        withdrawal_request = int(input('How much money would you like to withdraw? '))
        assert 0 <= withdrawal_request, "You can't withdraw a negative number. Please try again."
        assert withdrawal_request <= account_balance, "Insufficient funds. Please try again."
        assert withdrawal_request % 10 == 0, "You can only withdraw multiples of £10."
        print('Your withdrawal request of £{:.2f} has been accepted. Please take your cash'.format(withdrawal_request))
    except Exception as e:
        print(e)
    return withdrawal_request


def update_account_balance(account_balance, withdrawal_request):
    account_balance = account_balance - withdrawal_request
    print("Your new account balance is: £{:.2f}.".format(account_balance))
    return account_balance


def make_a_withdrawal(correct_pin, balance):
    if check_pin_is_correct(correct_pin) and set_account_balance(balance):
        request_withdrawal(set_account_balance(balance))
        update_account_balance((set_account_balance(balance)), (request_withdrawal(set_account_balance(balance))))
    # I'm not super happy about how this function is looking. There are a lot of parentheses!
    # I don't think this function aligns with the DRY principle...
    # I'm not sure if there's a way to write one big function, with all these little functions inside it?
    # I think this may have contributed to whatever it is that has reduced my ability to unit test this program.
    else:
        raise Exception("One of the steps failed")


if __name__ == '__main__':
    make_a_withdrawal(correct_pin=1234, balance=100)