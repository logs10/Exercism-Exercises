def primes(limit):
    multiples = set()
    numbers = range(2, limit + 1)
    for num in numbers:
        # Check if current num is in set of defined multiples
        if num not in multiples:
            # if not, find all multiples of num starting with its square, incrementing by num
            for multiple in range(num * num, limit + 1, num):
                # Add multiple to multiples set
                multiples.add(multiple)
    # Difference of starting numbers set and multiples set returns all primes
    return sorted(set(numbers) - multiples)
