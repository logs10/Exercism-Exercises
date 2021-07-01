import string


def translate(text):
    vowels = ''.join([x for x in string.ascii_lowercase if x in ['a', 'e', 'i', 'o', 'u']])
    consonants = ''.join([x for x in string.ascii_lowercase if x not in vowels])
    word = text.lower().strip()

    if word[0] in vowels or word[0:2] in ['xr', 'yt']:
        return word + 'ay'
    else:
        # check for range of consonants, if found, move to end of string
        i = 0
        for letter in word:
            if letter in consonants:
                i += 1
        # check 2nd condition after first range found
        # if word[0:i] == 'qu':
        #     return word[i:i + 1] + 'quay'
        # else:
        return word[i - 1:len(word)] + word[0:i - 1] + 'ay'

        # check for range of consonants


print(translate("chair"))
