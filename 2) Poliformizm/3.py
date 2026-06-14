class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year
    def set_month(self, month):
        self.month = month
    def set_day(self, day):
        self.day = day
    def get_year(self):
        return self.year
    def get_month(self):
        return self.month
    def get_day(self):
        return self.day

    def format(self):
        m = str(self.month)
        if len(m) == 1:
            m = "0" + m
        d = str(self.day)
        if len(d) == 1:
            d = "0" + d
        y = str(self.year)
        while len(y) < 4:
            y = "0" + y
        return m + "." + d + "." + y

class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year
    def set_month(self, month):
        self.month = month
    def set_day(self, day):
        self.day = day
    def get_year(self):
        return self.year
    def get_month(self):
        return self.month
    def get_day(self):
        return self.day

    def format(self):
        d = str(self.day)
        if len(d) == 1:
            d = "0" + d
        m = str(self.month)
        if len(m) == 1:
            m = "0" + m
        y = str(self.year)
        while len(y) < 4:
            y = "0" + y
        return d + "." + m + "." + y