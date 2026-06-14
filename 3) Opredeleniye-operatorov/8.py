class Queue:
    def __init__(self, *values):
        self.items = list(values)

    def __str__(self):
        if not self.items:
            return "[]"
        return "[" + " -> ".join(str(item) for item in self.items) + "]"

    def __add__(self, other):
        new_queue = Queue()
        new_queue.items = self.items + other.items
        return new_queue

    def __iadd__(self, other):
        self.items.extend(other.items)
        return self

    def __eq__(self, other):
        return self.items == other.items

    def __rshift__(self, n):
        if n >= len(self.items):
            return Queue()
        return Queue(*self.items[n:])

    def __next__(self):
        if len(self.items) <= 1:
            return Queue()
        return Queue(*self.items[1:])

    def append(self, *values):
        for value in values:
            self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def copy(self):
        new_queue = Queue()
        new_queue.items = self.items.copy()
        return new_queue

    def extend(self, other_queue):
        self.items.extend(other_queue.items)

    def next(self):
        return self.__next__()