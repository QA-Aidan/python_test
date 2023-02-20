# Just counts the number of items in a sequence

class Count:
    def __init__(self):
        pass

    def count(self, sequence, item):
        sum1 = 0
        for n in sequence:
            if n == item:
                sum1 += 1
        return sum1


counter = Count()
