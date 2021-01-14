class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # apply initial cleaning steps to given card string
        clean = self.card_num.replace(' ', '')
        if not clean.isdigit() or len(clean) <= 1:
            return False
        else:
            new = []
            # reverse the cleaned string, loop through digits and apply the rest of the algorithm
            for index, digit in enumerate(clean[::-1]):
                print(index, digit)
                if index % 2 != 0:
                    if (int(digit) * 2) > 9:
                        new.append((int(digit) * 2) - 9)
                    else:
                        new.append(int(digit) * 2)
                else:
                    new.append(int(digit))
        if sum(new) % 10 == 0:
            return True
        else:
            return False
