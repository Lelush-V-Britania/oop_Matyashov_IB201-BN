class GameSettings:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.volume = 50
            self.difficulty = "Normal"
            self._initialized = True