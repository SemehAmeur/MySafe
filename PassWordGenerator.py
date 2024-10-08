import string
import random


class PassWordGenerator:
        def charlistfunc(self, lowercase_char, uppercase_char, numbers_char, specialdigit_char):
        characterList = ""

        # Adding uppercase letters to possible characters
        if uppercase_char:
            characterList += string.ascii_uppercase

        # Adding lowercase letters to possible characters
        if lowercase_char:
            characterList += string.ascii_lowercase

        # Adding digits to possible characters
        if numbers_char:
            characterList += string.digits

        # Adding special characters to possible
        if specialdigit_char:
            characterList += string.punctuation
        return characterList
    def passgenerate():
        pass