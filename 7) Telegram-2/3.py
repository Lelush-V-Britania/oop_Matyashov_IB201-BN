class User:
    _counter = 0

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    @classmethod
    def create(cls, name: str) -> "User":
        cls._counter += 1
        return cls(name, cls._counter)

    @classmethod
    def count(cls) -> int:
        return cls._counter