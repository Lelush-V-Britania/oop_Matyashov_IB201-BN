class ReversedList:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

    def __getitem__(self, index):
        return self.list[-(index + 1)]