def response(phrase):
    """return bob's response to a question"""
    # clean phrase spaces
    phrase = ' '.join(phrase.split())

    # check various cases
    if phrase[-1:] == '?':
        if phrase.isupper() == True:
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif phrase[-1:] == '!':
        if phrase.isupper() == True:
            return "Whoa, chill out!"
        return "Whatever."
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif phrase.isspace() or len(phrase) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."
