def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) == 0: return 
    return lst[-1]

print(last_element([1, 2, 3]))
print(last_element([]))
print(last_element(['a', 'b', 'c']))