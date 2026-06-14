class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
            return
        dist_x = actor.get_coords()[0] - target.get_coords()[0]
        dist_y = actor.get_coords()[1] - target.get_coords()[1]
        distance = (dist_x ** 2 + dist_y ** 2) ** 0.5
        if distance > self.range:
            print(f"Враг слишком далеко для оружия {self.name}")
            return
        print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
        target.get_damage(self.damage)

    def __str__(self):
        return self.name

class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def get_coords(self):
        return (self.pos_x, self.pos_y)

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
            return
        self.weapon.hit(self, target)

    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"

class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon = None

    def hit(self, target):
        if self.current_weapon is None:
            print("Я безоружен")
            return
        if not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
            return
        self.current_weapon.hit(self, target)

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return
        self.weapons.append(weapon)
        if self.current_weapon is None:
            self.current_weapon = weapon
        print(f"Подобрал {weapon}")

    def next_weapon(self):
        if not self.weapons:
            print("Я безоружен")
            return
        if len(self.weapons) == 1:
            print("У меня только одно оружие")
            return
        current_index = self.weapons.index(self.current_weapon)
        next_index = (current_index + 1) % len(self.weapons)
        self.current_weapon = self.weapons[next_index]
        print(f"Сменил оружие на {self.current_weapon}")

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")