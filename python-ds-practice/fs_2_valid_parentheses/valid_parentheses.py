def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    mem = {"unresolved_par": 0}
    for par in parens:
        if par == "(":
            mem["unresolved_par"] += 1
        elif par == ")":
            mem["unresolved_par"] -= 1
            if mem["unresolved_par"] < 0:
                return False
      
    if mem["unresolved_par"] == 0:
        return True
    else:
        return False