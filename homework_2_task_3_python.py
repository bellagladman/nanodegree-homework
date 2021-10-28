"""
HOMEWORK 2
"""

"""
TASK 3 (Python)
Question 1
I am building some very high-quality chairs and need exactly four nails for each chair. 
I've written a program to calculate how many nails I need to buy to build these chairs.
 
chairs = '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))
 
When I run the program, it tells me that I need to buy 15151515 nails. This seems like a lot of nails. 
Is my program calculating the total number of nails correctly? What is the problem? 

No, the program isn't calculating the number of nails correctly.
In the code given above, the number of chairs (15) is given in inverted commas (‘’), 
which designates it as a string, rather than as an integer. 
In Python, multiplying a string by an integer n makes the string repeat itself n times, 
which is why the string saved into the variable chairs, ’15’ is repeated four times to give 15151515.

The second problem is that the print statement inserts message into the string formatting, 
so the output is: You need to buy I need to buy 15151515 nails nails

How do I fix it? To fix the first problem, simply remove the inverted commas ‘’ from around the number 15 
when it is saved into the chairs variable, like so:

chairs = 15

To fix the second problem, you have two options. 
One is to remove the variable message, and then change the string formatting 
in the print statement to read .format(total_nails) at the end, like so:

chairs = 15
nails = 4
total_nails = chairs * nails
print('You need to buy {} nails’.format(total_nails))

Which gives the output:
You need to buy 60 nails

Or, you can keep the message variable, and then change the print statement to read print(message).

chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)

Which gives the output:
I need to buy 60 nails
"""

"""
Question 2 
I'm trying to run this program, but I get an error. 

    my_name = Penelope
    my_age = 29
    message = 'My name is {} and I am {} years old'.format(my_name, my_age)
    print(message)

What is the error telling me is wrong? How do I fix the program?

The error is a NameError, specifically that the name 'Penelope' is not defined. 
Because Penelope should be treated as a string, it needs to have speech marks or inverted commas around it. 
Otherwise, Python might think it is a variable or another keyword.
You fix it by putting speech marks around ‘Penelope’, like so:

my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

"""

"""
Question 3 
I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make. 
Write a program to calculate this. Assume that a box of eggs contains six eggs 
and I need four eggs for each omelette, but I should be able to easily change these values if I want. 
The output should say something like "You can make 9 omelettes with 6 boxes of eggs". 

Here is my program:

boxes_of_eggs = int(input('How many boxes of eggs do you have? '))
omelettes = boxes_of_eggs * 1.5
print('You can make {} omelettes with {} boxes of eggs.'.format(omelettes, boxes_of_eggs))

"""

"""
Question 4
Complete a series of tasks to format strings
 
#Task 1 - Replace the (.) with (!)
my_str = "I love coding."
my_str = my_str.replace(".", "!")
print(my_str)

-----
I love coding!
"""

"""
#Task 2 - Reassign str so that all its characters are lowercase.
my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
my_str_1 = my_str_1.lower()
print(my_str_1)

----
every exercise brings me closer to completing my goals.
"""

"""
#Task 3 - Does the string start with an A?
my_str_2 = "We enjoy travelling"
if my_str_2.startswith('A'):
   ans_1 = 'Yes, the string starts with an A'
elif my_str_2.startswith('a'):
   ans_1 = 'Yes, the string starts with an A'
else:
   ans_1 = 'No, the string does not start with an A'
print(ans_1)

----
No, the string does not start with an A
"""

"""
#Task4 - What is the length of the given string?
my_str_3 = "1.458.001"
ans_2 = len(my_str_3)
print(ans_2)

----
9
"""

"""
Question 5
Complete a series of tasks to slice strings
 
#Task 1 - Slice the word so that you get "thon".
wrd="Python"
ans_1 = wrd[2:]
print(ans_1)

----
thon
"""

"""
#Task 2 - Slice the word until "o". (Pyth)
wrd="Python"
ans_1 = wrd[:4]
print(ans_1)

----
Pyth
"""

"""
#Task 3 - Now try to get "th" only.
wrd="Python"
ans_1 = wrd[2:4]
print(ans_1)

----
th
"""

"""
#Task 4 - Now slice the word with steps of 2, excluding first and last characters
wrd="Python"
ans_1 = wrd[1:-2:2]
print(ans_1)

----
yh
"""

"""
Question 6 
Explain what this program does
 
for number in range(100):
	output = 'o' * number
	print(output)

It prints a succession of the character o; the first row has zero o’s, 
the second has one o, and so forth up until the 100th row which has 99 o’s.

"""

"""
Question 7 
Your boss really likes calculating VAT on their purchases. 
It is their favourite hobby. 
They’ve written this code to calculate VAT and need your help to fix it.
 
    def calculate_vat(amount):
        amount * 1.2
    total = calculate_vat(100)
    print(total)
 
When your boss runs the program they get the following output: None. 
Your boss expects the program to output the value 120. What is wrong? How do you fix it?

Functions always return a value, and if the return value is not set, 
then it will automatically be None. In the code above, the return value has not been set, 
which is why the output is None and not 120.

To fix it, set the return value to amount * 1.2, 
so that the function calculate_vat returns what it calculates, like so:

    def calculate_vat(amount):
        return amount * 1.2
    
    total = calculate_vat(100)
    print(total)
"""

"""
Question 8 
Write a new function to print a ‘cashier receipt’ output for a shop (any shop – clothes, food, events etc).
It should accept 3 items, then sum them up and print out a detailed receipt with TOTAL.
 
For example (input):
Item_1_name = ‘Trainers’
Item_1_price = 50.45
Item_2_name = ‘T-shirt
Item_2_price = 12
 
Output:
Trainers …….50.45
T-shirt………..12.00
TOTAL       	62.45
 
 
Here is my code: 

def get_receipt(item1name, item1price, item2name, item2price, item3name, item3price):
   print(item1name + '.........£' + str(item1price))
   print(item2name + '.........£' + str(item2price))
   print(item3name + '.........£' + str(item3price))
   totalPrice = (item1price + item2price + item3price)
   print("YOUR TOTAL IS £{}".format(totalPrice))

If I call the function:
	get_receipt('sweater', 5, 'trousers', 6, 'hat', 7)

The result:

Sweater.........£5
Trousers.........£6
Hat.........£7
YOUR TOTAL IS £18
"""




