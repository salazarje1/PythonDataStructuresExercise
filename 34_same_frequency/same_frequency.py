from tkinter import N


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)

    counter1 = {}
    counter2 = {}
    
    for num in num1:
        if num in counter1:
            counter1[num] += 1
        else: 
            counter1[num] = 1 
    
    for num in num2:
        if num in counter2:
            counter2[num] += 1
        else: 
            counter2[num] = 1 

    if counter1 == counter2: 
        print(True)
        return 
    else: 
        print(False)

    





same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)