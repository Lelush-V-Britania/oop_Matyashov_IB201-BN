class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates

    def __add__(self, other):
        new_proteins = self.proteins + other.proteins
        new_fats = self.fats + other.fats
        new_carbohydrates = self.carbohydrates + other.carbohydrates
        return FoodInfo(new_proteins, new_fats, new_carbohydrates)