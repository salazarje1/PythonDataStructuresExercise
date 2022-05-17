from typing import List


def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_list = list(phrase)
    new_list.reverse()
    phrase = "".join(new_list)
    print(phrase)


reverse_string('awesome')
reverse_string('sauce')