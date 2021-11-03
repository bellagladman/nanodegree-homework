"""
Question 3:
Write a function that can check if a word is a palindrome or not
"""


def lowercase_the_word(word):
    new_word = word.strip()
    new_word = new_word.casefold()
    return new_word


def reverse_the_word(word):
    word = word.casefold()
    reversed_word = word[::-1]
    return reversed_word


def palindrome_check(word, reversed_word):
    if word == reversed_word:
        return True
    else:
        return False


my_word = 'Appa'
my_lowercased_word = lowercase_the_word(my_word)
my_reversed_word = reverse_the_word(my_lowercased_word)
print(my_lowercased_word)
print(my_reversed_word)
print(palindrome_check(my_lowercased_word, my_reversed_word))