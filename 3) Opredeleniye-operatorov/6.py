class SparseArray:
    def __init__(self):
        self.data = {}

    def __getitem__(self, index):
        if index in self.data:
            return self.data[index]
        else:
            return 0

    def __setitem__(self, index, value):
        if value != 0:
            self.data[index] = value
        else:
            if index in self.data:
                del self.data[index]