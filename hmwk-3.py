"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate the required word/phrase using the characters provided.
If you can, return True. Otherwise, return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

characters = "cbacba"
phrase = "aabbccc"


class PhraseSplitter:

    def __init__(self, characters, phrase):
        self.characters = characters
        self.phrase = phrase

    # def split_word(self, string):
    #     return [char for char in string]

    def generate_phrase(self, characters, phrase):
        if len(phrase) > len(characters):
            return "You cannot make the required phrase - you don't have enough characters!"


def split_word(string):
    string_list = [char for char in string]
    return string_list


def split_into_list(string):
    new_list = list(string)
    return new_list


print(split_word(characters))
print(split_into_list(characters))


