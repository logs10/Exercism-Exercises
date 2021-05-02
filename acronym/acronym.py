def abbreviate(words):
    # for a given phrase represented by a string, return the corresponding acronym
    # solved without using Regular Expressions
    words_str = ''
    for letter in words:
        if letter == "'" or letter.isalnum() or letter == ' ':
            words_str = words_str + letter
        elif letter == '-':
            words_str = words_str + letter
        else:
            pass
    clean_list = words_str.replace('-', ' ').split(' ')
    # further cleaning, removing empty string elements
    clean_list[:] = [x for x in clean_list if x]
    return ''.join([x[0].upper() for x in clean_list])
