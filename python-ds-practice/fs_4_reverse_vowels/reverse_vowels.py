def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    phrase = ""
    vowels = []
    for letter in s:
        if letter.lower() in "aeiou":
            phrase += "~"
            vowels.append(letter)
        else: 
            phrase += letter
    
    index = 0
    new_phrase = ""
    vowels = vowels[-1:-len(vowels)-1:-1]
    
    for letter in phrase:

        if letter == "~":
            new_phrase += vowels[index]
            index += 1
        else:
            new_phrase += letter

    return new_phrase