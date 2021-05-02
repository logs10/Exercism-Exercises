
def compute(clean_isbn):
    # for valid looking isbn's, compute score and return bool
    score = []
    for index, digit in enumerate(clean_isbn):
        if digit == 'X':
            val = 10
        elif digit.isdigit() == False:
            val = 0
        else:
            val = digit
        score.append(int(val) * (10 - index))
    if sum(score) % 11 == 0:
        return True
    else:
        return False


def is_valid(isbn):
    # clean provided isbn string and pre-check validity
    if isbn == '':
        return False
    else:
        clean_isbn = isbn.replace('-', '')
        last_char = clean_isbn[len(clean_isbn) - 1]
        for digit in clean_isbn[:-1]:
            if digit.isdigit() == False:
                return False
        if len(clean_isbn) != 10:
            return False
        else:
            return compute(clean_isbn)
