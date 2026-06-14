class Date:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def day_of_year(self):
        days = self.day
        for m in range(self.month - 1):
            days += Date.month_days[m]
        return days

    def __sub__(self, other):
        return self.day_of_year() - other.day_of_year()