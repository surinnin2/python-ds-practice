def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    list1 = []
    list2 = []
    dict1 = {}
    dict2 = {}
    for num in str(num1):
        list1.append(int(num))
    for num in str(num2):
        list2.append(int(num))

    set1 = set(list1)
    set2 = set(list2)

    for num in set1:
        dict1.update({num: list1.count(num)})
    for num in set2:
        dict2.update({num: list2.count(num)})

    if dict1 == dict2:
        return True
    else:
        return False