def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = [char.lower().capitalize() for char in phrase.split()]
    title = ' '.join(lst)


    print(title)

titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')
