def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if isinstance(num, int) and num > 0:
        print(phrase * num)
    elif num == 0: 
        print('')
    else:
        print(None)

repeat('*', 3)
repeat('abc', 2)
repeat('abc', 0)
repeat('abc', -1)
repeat('abc', 'nope')