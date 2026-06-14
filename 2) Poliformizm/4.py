class MinStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def result(self):
        if len(self.numbers) == 0:
            return None
        minimum = self.numbers[0]
        for x in self.numbers:
            if x < minimum:
                minimum = x
        return minimum

class MaxStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def result(self):
        if len(self.numbers) == 0:
            return None
        maximum = self.numbers[0]
        for x in self.numbers:
            if x > maximum:
                maximum = x
        return maximum

class AverageStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def result(self):
        if len(self.numbers) == 0:
            return None
        total = 0
        for x in self.numbers:
            total = total + x
        return total / len(self.numbers)