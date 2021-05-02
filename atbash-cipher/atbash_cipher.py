import string
from collections import defaultdict


def clean_dicts(text):
    """
    Helper function that takes a text string and returns a tuple of:
        1) A cleaned version of the text string with only alphanumeric characters
        2) A dictionary containing sequential letters of the alphabet and the resspective letter index value
        3) A reversed dictionary with keys/values reversed for easier lookup
    """
    clean_txt = ''.join(x for x in text if x.isalnum())
    letter_dict = {k: v for v, k in enumerate(string.ascii_lowercase)}
    reverse_letter_dict = defaultdict(str)
    for key, value in letter_dict.items():
        reverse_letter_dict[value] = key
    return (clean_txt, letter_dict, reverse_letter_dict)


def encode(plain_text):
    """
    Given a text string, implement and return the results of the atbash cipher algorithm.
    """
    clean_txt, l_dict, r_dict = clean_dicts(plain_text)
    output = ''
    counter = 1
    print(clean_txt)
    for char in clean_txt:
        if char.isalpha():
            new_loc = 25 - (l_dict[char.lower()])
            if counter < 5:
                output = output + r_dict[new_loc]
                counter += 1
            else:
                output = output + r_dict[new_loc] + ' '
                counter = 1
        else:
            if counter < 5:
                output = output + char
                counter += 1
            else:
                output = output + char + ' '
                counter = 1
    return output.strip()


def decode(ciphered_text):
    """
    Given a encoded text string from the atbash cipher algorithm, decode and return the results of the original text input.
    """
    clean_txt, l_dict, r_dict = clean_dicts(ciphered_text)
    output = ''
    for char in clean_txt:
        if char.isalpha():
            loc = 25 - (l_dict[char.lower()])
            output = output + r_dict[loc]
        else:
            output = output + char
    return output.strip()
