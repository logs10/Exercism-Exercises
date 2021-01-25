def is_armstrong_number(number):
    num_len = len(str(number))
    nums = [int(x)**int(num_len) for x in str(number)]
    if sum(nums) == int(number):
        return True
    else:
        return False
