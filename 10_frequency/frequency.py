def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    counter = 0
    for num in lst: 
        if num == search_term:
            counter += 1

    print(counter)

frequency([1, 4, 3, 4, 4], 4)
frequency([1, 4, 3], 7)