from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

class Lion(Animal):
    def make_sound(self) -> str:
        return "Рычание!"

class Monkey(Animal):
    def make_sound(self) -> str:
        return "Визг!"

class Elephant(Animal):
    def make_sound(self) -> str:
        return "Трубление!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()

class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()

class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()

def interact_with_animal(factory: AnimalFactory) -> None:
    animal = factory.create_animal()
    print(f"Звук: {animal.make_sound()}")