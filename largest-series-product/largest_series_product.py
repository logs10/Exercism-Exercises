from math import prod


def largest_product(series, size):
    if series == "" and size == 0:
        return 1
    elif size < 0 or size > len(series):
        raise ValueError("Invalid inputs entered.")
    else:
        current = 0
        largest = 0
        nums = [int(x) for x in series]
        for index, num in enumerate(series):
            val_list = nums[current:current + size]
            if len(val_list) == size:
                product = prod(val_list)
                if product > largest:
                    largest = product
                current += 1
        return largest
