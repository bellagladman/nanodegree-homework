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

chars1 = "ab ba"
phrase1 = " abba"


def phrase_checker(characters, phrase):
    list1 = [characters, phrase]

    def split_into_list(string):
        string_list = list(string)
        return string_list

    for index, item in enumerate(list1):
        list1[index] = split_into_list(list1[index])

    for item in list1:
        item.sort()

    if list1[0] == list1[1]:
        return "You can generate the given phrase '{}' with the given characters '{}'.".format(phrase, characters)
    elif len(list1[1]) > len(list1[0]):
        return "You don't have enough characters in the given set '{}' to make the given phrase '{}'.".format(characters, phrase)
    else:
        return "You can't generate this phrase '{}' with these characters '{}'.".format(phrase, characters)

print(phrase_checker(characters, phrase))
print(phrase_checker(chars1, phrase1))











