class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def from_string(cls, s: str) -> "Point":
        parts = s.replace(" ", "").split(",")
        return cls(float(parts[0]), float(parts[1]))

    @classmethod
    def from_dict(cls, d: dict) -> "Point":
        return cls(d["x"], d["y"])

    @staticmethod
    def distance(a: "Point", b: "Point") -> float:
        return round(((a.x - b.x)**2 + (a.y - b.y)**2)**0.5, 2)