from itertools import combinations_with_replacement


def total(basket):
    discounts = {1: 0,
                 2: 0.05,
                 3: 0.1,
                 4: 0.2,
                 5: 0.25}
    if len(basket) == 0:
        return 0
    # Define number of books in the basket
    num_books = len(basket)
    # Define dictionary with counts of all unique books in the basket
    books = {}
    for book in basket:
        books[book] = books.get(book, 0) + 1
    # Max number of any given book to determine total sets needed
    max_books = max(books.values())
    # Determine largest possible number of books per set
    max_size = len(books.keys())
    # Get possible lengths of sets, only look at sets that are valid based on number of given books
    carts = []
    for combo in combinations_with_replacement(range(1, max_size + 1), max_books):
        # Only look at valid combos
        if sum(combo) <= num_books:
            # Store remaining books in cart after valid discount combo
            remaining_books = num_books - sum(combo)
            discount_price = []
            # Calculate discounted prices using discount factors
            for i in combo:
                price = i * 8
                discount = discounts[i]
                total = price - (price * discount)
                discount_price.append(total)
            cart_price = sum(discount_price)
            cart_price = cart_price + (remaining_books * 8)
            carts.append(cart_price)
            # Return the minimum cart price
    return int('{:.2f}'.format(min(carts)).replace('.', ''))
