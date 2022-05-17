def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    counter = 0 
    for ltr in word.lower(): 
        if ltr == letter: 
            counter += 1

    print(counter)


single_letter_count('Hello World', 'h')
single_letter_count("Hello World", 'l')
single_letter_count('Hello World', 'z')