from itertools import combinations_with_replacement


def combo_gen(coins, iterration, target):
    # define combination generator function to yield/return all valid combinations
    # for the given iterration
    combo = list(combinations_with_replacement(coins, iterration))
    for i in combo:
        if sum(i) == target:
            yield list(i)


def find_fewest_coins(coins, target):
    # handle edge cases with weird params
    if target < 0:
        raise ValueError("Incorrect input parameters.")
    if target == 0:
        return []
    else:
        # for each iteration until target value, generate all possible coin combinations
        # from given coins that sum to target value. The optimal solution (lowest number of coins)
        # will be the first valid combination in the loop
        solution = True
        for i in range(1, target + 1):
            check = list(combo_gen(coins, i, target))
            if len(check) > 0:
                return check[0]
            else:
                solution = False
        if solution == False:
            raise ValueError("Incorrect input parameters.")
