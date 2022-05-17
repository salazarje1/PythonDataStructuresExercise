def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    dup_num = 0

    while len(nums) != dup_num: 
        print(dup_num)
        if nums.count(dup_num) > 1:
            print(dup_num)
            return 
        else: 
            dup_num += 1
            
    
    return None


find_the_duplicate([1, 2, 1, 4, 3, 12])
find_the_duplicate([6, 1, 9, 5, 3, 4, 9, 10])
find_the_duplicate([2, 1, 3, 4])