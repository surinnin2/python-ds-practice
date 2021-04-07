def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    to_return = phrase[0].upper() + phrase[1:len(phrase)]
    return to_return