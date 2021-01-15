

def rotate(text, key):
    # Given a string, create a dictionary consisting of all elements within the string and their
    # respective index values as keys. This will help preserve order when using modular arithmetic
    # on the string
    alpha_list, letter_dict = [], {}
    # create list of alphabetic characters
    for letter in range(97, 123):
        alpha_list.append(chr(letter))
    # Double the
    clean_list = ''.join(alpha_list + alpha_list)
    for index, char in enumerate(clean_list):
        letter_dict[index] = char
    # Formatting characteristics need to be maintained in calculated output, so create a list of lists
    # containing this information for each element from the given string as well as the before/after
    # alphabetic character of the calculated rotational cipher
    replace_map = []
    for char in text:
        element = []
        if char.isalpha() == True:
            if char.isupper() == True:
                element.append('upper')
            elif char.isupper() == False:
                element.append('lower')
        # not an alphabetic character, return the character as is to preserve formatting
        else:
            element.append(char)
        # Calculate the rotational cipher for each element using defined letter dictionary
        for k, val in letter_dict.items():
            if k <= 25:
                if char.lower() == val:
                    pos = k
                    new_pos = k + key
                    element.append(
                        [letter_dict[pos], letter_dict[new_pos]])
        replace_map.append(element)
    # Using the templated values, loop through the replace_map list object and build the finished output
    final = []
    for element in replace_map:
        if element[0] == 'upper':
            final.append(element[1][1].upper())
        elif element[0] == 'lower':
            final.append(element[1][1])
        else:
            final.append(element[0])

    return str(''.join(final))
