def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    d = {}

    for letter in phrase:
        d[letter] = d.get(letter, 0) + 1

    ordered_d = {key: d[key] for key in sorted(d.keys(), key=d.__getitem__, reverse=True)}

    return ordered_d