class Selector:
    def __init__(self, values):
        self.values = values

    def get_odds(self):
        res = []
        for x in self.values:
            if x % 2 != 0:
                res.append(x)
        return res

    def get_evens(self):
        res = []
        for x in self.values:
            if x % 2 == 0:
                res.append(x)
        return res