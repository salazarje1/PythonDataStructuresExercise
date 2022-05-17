import re


def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.replace(' ', '')

    reversed_phrase = list(phrase)
    reversed_phrase.reverse()
    reversed_phrase = "".join(reversed_phrase)

    if phrase.lower() == reversed_phrase.lower():
        print(True)
    else:
        print(False)


is_palindrome('tacocat')
is_palindrome('noon')
is_palindrome('robert')

is_palindrome('Noon')
is_palindrome('taco cat')