"""
Testing
"""

import string

alphabet = string.ascii_lowercase

def find_consonant_range(text, consonants):
    i = 0
    for letter in text:
        if letter in consonants:
            i += 1
    return i

def translate(text):
    vowels = [x for x in alphabet if x in ['a', 'e', 'i', 'o', 'u']]
    consonants = [x for x in alphabet if x not in vowels]
    first_letter = text[0:1].lower()
    first_two_letters = text[0:2].lower()
    result = ""
    if first_letter in vowels or first_two_letters in ['xr', 'yt']:
        result = text + 'ay'
    elif first_letter in consonants:
        if text[1:2] in 'qu':
            text = text[0:2]
            end_range = find_consonant_range(text, consonants)
            result = text[end_range - 1:len(text)] + text[0:end_range - 1] + 'ay'
        else:
            end_range = find_consonant_range(text, consonants)
            result = text[end_range - 1:len(text)] + text[0:end_range - 1] + 'ay'
    return result

print(translate("square"))