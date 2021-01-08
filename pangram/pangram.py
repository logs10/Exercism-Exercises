
def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    letters = set()

    for character in sentence:
        if character.isalpha():
            letters.add(character)

    return len(letters) == 26
