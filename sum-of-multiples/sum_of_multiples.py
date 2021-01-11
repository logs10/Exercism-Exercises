def sum_of_multiples(limit, multiples):
    valid_multiples = set()
    for number in range(1, limit):
        for multiple in multiples:
            if multiple == 0:
                pass
            elif number % multiple == 0:
                valid_multiples.add(number)
    return sum(valid_multiples)
