

def return_val(letter):
    # Define letter scores
    # List of tuples containing a list of letters and respective scores
    scores = [
        (['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
        (['D', 'G'], 2),
        (['B', 'C', 'M', 'P'], 3),
        (['F', 'H', 'V', 'W', 'Y'], 4),
        (['K'], 5),
        (['J', 'X'], 8),
        (['Q', 'Z'], 10)]

    # return score for given letter
    for entries in scores:
        if letter in [x.lower() for x in entries[0]]:
            return entries[1]


def score(word):
    # compute score from given word
    # create dictionary to hold unique letters seen in word and
    # respective counts
    scorecard = {}
    for letter in word.lower():
        scorecard[letter] = 0
    for key in scorecard.keys():
        count = 0
        for letter in word.lower():
            if key == letter:
                count += 1
                letter_score = return_val(key)
        scorecard[key] = (count, letter_score)

    score_list = []
    for key, values in scorecard.items():
        score_list.append(values[0] * values[1])
    return sum(score_list)
