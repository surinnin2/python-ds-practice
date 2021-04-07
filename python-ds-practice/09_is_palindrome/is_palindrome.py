def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    str = phrase.lower().replace(" ", "")
    first_half = int(len(str)/2)
    second_half = int(-len(str)/2)
    if str[0: first_half] == str[-1: second_half: -1]:
        return True
    elif:
        return False
    