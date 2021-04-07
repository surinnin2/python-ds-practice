def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    str = ""
    for index in range(1, len(phrase) + 1):
        str.append(phrase[-index])
    return str