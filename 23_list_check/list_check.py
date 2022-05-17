def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for item in lst: 
        if not isinstance(item, list):
            print(False)
            return 
    print(True)


list_check([[1], [2, 3]])
list_check([[1], "nope"])