"""
HOMEWORK 3
CFG NANODEGREE / SOFTWARE 3
ISOBEL GLADMAN
"""

"""
TASK 1 (Conditional flow)

Question 1
Create a program that tells you whether or not you need an umbrella when you leave the house.
The program should:
1. Ask you if it is raining using input()
2. If the input is 'y', it should output 'Take an umbrella'
3. If the input is 'n', it should output 'You don't need an umbrella'

Here is my program:

is_it_raining = input('Is it raining right now? y/n ')

if is_it_raining == 'y' or is_it_raining == 'Y':
   print('Take an umbrella!')
elif is_it_raining == 'n' or is_it_raining == 'N':
   print("You don't need an umbrella.")
else:
   print("Please re-run the program and answer whether it is raining right now with y/n.")
"""

"""
Question 2
I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've written a program to check that I can afford the cost, but something doesn't seem right. Have a look at my program and work out what I've done wrong
my_money = input('How much money do you have? ')
boat cost = 20 + 5

if my_money < boat_cost:
	print('You can afford the boat hire')
else :
	print('You cannot afford the board hire'

One problem is that the variable name boat cost can’t have a space in it - it should be all connected as if one word ie. boatcost; written in camel case i.e. boatCost, or in snake case i.e. boat_cost. Later in the program it is referred to as boat_cost, so this is the best choice. Essentially, we need to make sure the variable has the same name both when it is defined and also when it is referred to later.

The second problem is that the input() function returns a string, and the value saved in boat_cost is an integer. You can’t compare a string and an integer to see which is larger, so the if statement won’t work. To fix this, you could cast the input function so that it returns an integer, using the int() method.

The third problem is that the if...else statement doesn’t make sense. If the user enters that they have more money than what the boat hire costs, the print statement says that they can’t afford it, which obviously isn’t true. To fix this, you’d need to swap the print statements, so that if my_money is less than boat_cost, it says that you can’t afford it. The second print statement in the above program also mentions board hire (which is weird, because we’re talking about boat hire). You’d fix this by changing the word ‘board’ to ‘boat’ in the string.
The final problem is that the program is missing a parenthesis at the end of the last print statement - to fix it, you’d just make sure you close the print statement with a closing bracket.

The fixed code would look like this:

my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5

if my_money < boat_cost:
  print('You cannot afford the boat hire')
else :
  print('You can afford the boat hire')
"""

"""
Question 3
Your friend works for an antique book shop that sells books between 1800 and 1950 and
wants to quickly categorise books by the century and decade that they were written.
Write a program that takes a year (e.g.1872) and outputs the century and decade
(e.g."Nineteenth Century, Seventies")

Here is my program:

book_year = input('What year is the book from? ')

is19thc = book_year.startswith('18')
is20thc = book_year.startswith('19')

if is19thc:
    print('Nineteenth century')
elif is20thc:
    print('Twentieth century')
else:
    print('Sorry, we only stock books from between 1800 and 1950. Please choose a date within that range.')

book_year = int(book_year)

if book_year < 1800 or book_year > 1950:
    print("Sorry we only stock books from between 1800 and 1950.")
elif (1800 <= book_year <= 1809) or (1900 <= book_year <= 1909):
    print('Decade: Noughties')
elif (1810 <= book_year <= 1819) or (1910 <= book_year <= 1919):
    print('Decade: Tens')
elif (1820 <= book_year <= 1829) or (1920 <= book_year <= 1929):
    print('Decade: Twenties')
elif (1830 <= book_year <= 1839) or (1930 <= book_year <= 1939):
    print('Decade: Thirties')
elif (1840 <= book_year <= 1849) or (1940 <= book_year <= 1949):
    print('Decade: Forties')
elif (1850 <= book_year <= 1859) or (book_year == 1950):
    print('Decade: Fifties')
elif 1860 <= book_year <= 1869:
    print('Decade: Sixties')
elif 1870 <= book_year <= 1879:
    print('Decade: Seventies')
elif 1880 <= book_year <= 1889:
    print('Decade: Eighties')
elif 1890 <= book_year <= 1899:
    print('Decade: Nineties')
"""

"""
TASK 2(Lists and Dictionaries)

Question 1
I have a list of things I need to buy from my supermarket of choice.

    shopping_list = [
        "oranges",
        "cat food",
        "sponge cake",
        "long-grain rice",
        "cheese board",
    ]
    print(shopping_list[1])

I want to know what the first thing I need to buy is.
However, when I run the program it shows me a different answer to what I was expecting?
What is the mistake? How do I fix it?

Python starts counting indexes from 0, so requesting the value at index 1 is, in fact, asking
for the second item on the list. To get the very first item, the print statement
would need to read print(shopping_list[0]), as shown below:

    shopping_list = [
        "oranges",
        "cat food",
        "sponge cake",
        "long-grain rice",
        "cheese board",
    ]
print(shopping_list[0])
"""

"""
Question 2
I'm setting up my own market stall to sell chocolates. '
I need a basic till to check the prices of different chocolates that I sell.
I've started the program and included the chocolates and their prices.'
Finish the program by asking the user to input an item and then output its price.
    chocolates = {
        'white': 1.50,
        'milk': 1.20,
        'dark': 1.80,
        'vegan': 2.00,
    }

Here is my program:

chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

customer_choc_choice = input('Select your chocolate from: white, milk, dark, vegan: ')
print("Your choice of {} chocolate costs £{}".format(customer_choc_choice, chocolates[customer_choc_choice]))
"""

"""
Question 3
Write a program that simulates a lottery.The program should have a list
of seven numbers that represent a lottery ticket.It should then generate
seven random numbers.After comparing the two sets of numbers, the program
should output a prize based on the number of matches:

£20 for three matching numbers
£40 for four matching numbers
£100 for five matching numbers
£10000 for six matching numbers
£1000000 for seven matching numbers

Here is my solution:

import random

# GETTING THE USER'S LOTTERY NUMBER PICKS
lottery_picks = input('Select seven lottery numbers between 1 and 50: ')
lottery_picks = lottery_picks.split()

for i in range(7):
    lottery_picks[i] = int(lottery_picks[i])

lottery_picks = sorted(lottery_picks)
print('The lottery numbers you selected were: {}'.format(lottery_picks))

# GENERATING LOTTERY WINNERS
lottery_winners = []
for i in range(7):
    random_integer = random.randint(1, 50)
lottery_winners.append(random_integer)
lottery_winners = sorted(lottery_winners)
print('The winning numbers are :{}'.format(lottery_winners))

# CHECKING MATCHES
# add one list to the other
lottery_winners.extend(lottery_picks)
# turn that total list into a set
lottery_winners = set(lottery_winners)
# the set removes duplicates (i.e. matches)
# count how many items are left in the set (because matches will have been removed)
# take that away from 14 (the total of the two lists of numbers)
number_of_matches = 14 - (len(lottery_winners))
print('You matched {} number(s).'.format(number_of_matches))

# LETTING THE USER KNOW IF THEY'RE A WINNER
if number_of_matches < 3:
    print("Sorry, you're not a winner this time.")
elif number_of_matches == 3:
    print("You win £20!")
elif number_of_matches == 4:
    print("You win £40!")
elif number_of_matches == 5:
    print("You win £100!")
elif number_of_matches == 6:
    print("You win £10,000!")
elif number_of_matches == 7:
    print("You win £1,000,000 pounds!")
"""

"""
TASK 3(Read and Write files)
Question 1
You 're having coffee/tea/beverage of your choice with a friend that is learning to program in
Python.They 're curious about why they would use pip. Explain what pip is and one benefit of using pip.

Pip is a package manager in Python. Using pip, you can install modules and libraries of code that
aren’t included in your basic Python package. This basically saves you a lot of time, because it
means that instead of having to write code entirely alone, you can just reuse code that other people
have written and then build on top of that, by importing modules/libraries that other people have written
and made available for others to use.
"""

"""
Question 2
This program should save my data to a file, but it doesn't work when I run it. '
What is the problem and how do I fix it?

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'r') as poem_file:
    poem_file.write(poem)

To write to a file, you need to open the file in write mode, i.e. with ‘w’ instead of ‘r’.
To make it work, you could use code like the below:

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)
"""

"""
Question 3
Here is a snippet of Elton John’s song “I’m Still Standing”
 
You could never know what it's like
Your blood like winter freezes just like ice
And there's a cold lonely light that shines from you
You'll wind up like the wreck you hide behind that mask you use
 
And did you think this fool could never win?
Well look at me, I'm coming back again
I got a taste of love in a simple way
And if you need to know while I'm still standing, you just fade away
 
Don't you know I'm still standing better than I ever did
Looking like a true survivor, feeling like a little kid
I'm still standing after all this time
Picking up the pieces of my life without you on my mind
 
I'm still standing (Yeah, yeah, yeah)
I'm still standing (Yeah, yeah, yeah)
 
Tasks:
1.   	Write the lyrics to a new file called song.txt
2.   	Check that a file has been created successfully.
3.   	Then read lines from this file and print out ONLY those lines that have a word ‘still’ in them. 

Here is my program:


elton_john_im_still_standing_lyrics = "You could never know what it's like \n Your blood like winter freezes just like ice \n And there's a cold lonely light that shines from you \n You'll wind up like the wreck you hide behind that mask you use \n \n And did you think this fool could never win? \n Well look at me, I'm coming back again \n I got a taste of love in a simple way \n And if you need to know while I'm still standing, you just fade away\n \n Don't you know I'm still standing better than I ever did \n Looking like a true survivor, feeling like a little kid \n I'm still standing after all this time \n Picking up the pieces of my life without you on my mind \n \n I'm still standing (Yeah, yeah, yeah) \n I'm still standing (Yeah, yeah, yeah)"

with open('song.txt', 'w+') as elton_file:
    elton_file.write(elton_john_im_still_standing_lyrics)

with open('song.txt', 'r') as text:
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split()

        for word in words:
            if word == 'still':
                print(line)

"""

"""
TASK 4 (API)
Question 1
In this session you used the Pokémon API to retrieve a single Pokémon.
I want a program that can retrieve multiple Pokémon and save their names and moves to a file.
Use a list to store about 6 Pokémon IDs. Then in a for loop call the API to retrieve the data for each Pokémon. Save their names and moves into a file called 'pokemon.txt'

pokemon_ids = input("Please list six Pokemon ID numbers: ")
pokemon_ids = pokemon_ids.split()
print("The poke IDs split into a list of strings: {}".format(pokemon_ids))

import requests
from pprint import pprint as pp

for p in pokemon_ids:
   p = int(p)
   endpoint = 'http://pokeapi.co/api/v2/pokemon/{}'.format(p)

   response = requests.get(endpoint)
   pokemon = response.json()

   with open('pokemon-names-and-moves.txt', 'a+') as text_file:
       poke_name = pokemon['name']
       poke_name = poke_name.title()
       text_file.write(poke_name + '\n')
       moves = [[move['move']['name']] for move in pokemon['moves']]
       moves = str(moves)
       text_file.write('Moves: ' + moves + '\n')
"""

"""
Question 2 (optional)
Here is a link to a really cool API: https://opentdb.com/
Answer the following questions:
·        What is the name of this API?
·        What does it do?
·        Example URL to make a call to this API?
·        Example output?

The name of this API is Open Trivia Database. It allows you to retrieve trivia questions in your programming.

An example URL to make a call to this API: https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean

Example output:

/Users/bellagladman/PycharmProjects/nanodegree/venv/bin/python /Users/bellagladman/PycharmProjects/nanodegree/homeworks/homework3-api.py
{'response_code': 0,
 'results': [{'category': 'General Knowledge',
              'correct_answer': 'True',
              'difficulty': 'easy',
              'incorrect_answers': ['False'],
              'question': 'Gumbo is a stew that originated in Louisiana.',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'False',
              'difficulty': 'easy',
              'incorrect_answers': ['True'],
              'question': 'It is automatically considered entrapment in the '
                          'United States if the police sell you illegal '
                          'substances without revealing themselves.',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'False',
              'difficulty': 'easy',
              'incorrect_answers': ['True'],
              'question': 'Nutella is produced by the German company Ferrero.',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'True',
              'difficulty': 'easy',
              'incorrect_answers': ['False'],
              'question': 'On average, at least 1 person is killed by a drunk '
                          'driver in the United States every hour.',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'False',
              'difficulty': 'easy',
              'incorrect_answers': ['True'],
              'question': 'Pluto is a planet.',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'False',
              'difficulty': 'easy',
              'incorrect_answers': ['True'],
              'question': 'Adolf Hitler was born in Australia. ',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'True',
              'difficulty': 'easy',
              'incorrect_answers': ['False'],
              'question': 'The Lego Group was founded in 1932.',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'True',
              'difficulty': 'easy',
              'incorrect_answers': ['False'],
              'question': 'Romanian belongs to the Romance language family, '
                          'shared with French, Spanish, Portuguese and '
                          'Italian. ',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'False',
              'difficulty': 'easy',
              'incorrect_answers': ['True'],
              'question': 'Dihydrogen Monoxide was banned due to health risks '
                          'after being discovered in 1983 inside swimming '
                          'pools and drinking water.',
              'type': 'boolean'},
             {'category': 'General Knowledge',
              'correct_answer': 'False',
              'difficulty': 'easy',
              'incorrect_answers': ['True'],
              'question': 'Vietnam&#039;s national flag is a red star in front '
                          'of a yellow background.',
              'type': 'boolean'}]}
"""

