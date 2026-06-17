from abc import ABC, abstractmethod

class Engine:
    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        return f'Двигатель типа {self.type}'

class Transmission:
    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        return f'Коробка передач типа {self.type}'

class Body:
    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        return f'Кузов типа {self.type}'

class Car:
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def __str__(self):
        return f'{self.components}'

class BuilderInterface(ABC):
    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_transmission(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class CarBuilder(BuilderInterface):
    def __init__(self):
        self._car = Car()

    def build_engine(self):
        self._car.add(Engine(type=""))

    def build_transmission(self):
        self._car.add(Transmission(type=""))

    def build_body(self):
        self._car.add(Body(type=""))

    def get_result(self):
        return self._car

class SedanBuilder(BuilderInterface):
    def __init__(self):
        self._car = Car()

    def build_engine(self):
        self._car.add(Engine(type="Sedan"))

    def build_transmission(self):
        self._car.add(Transmission(type="Sedan"))

    def build_body(self):
        self._car.add(Body(type="Sedan"))

    def get_result(self):
        return self._car

class SUVBuilder(BuilderInterface):
    def __init__(self):
        self._car = Car()

    def build_engine(self):
        self._car.add(Engine(type="SUV"))

    def build_transmission(self):
        self._car.add(Transmission(type="SUV"))

    def build_body(self):
        self._car.add(Body(type="SUV"))

    def get_result(self):
        return self._car

class SportsCarBuilder(BuilderInterface):
    def __init__(self):
        self._car = Car()

    def build_engine(self):
        self._car.add(Engine(type="SportsCar"))

    def build_transmission(self):
        self._car.add(Transmission(type="SportsCar"))

    def build_body(self):
        self._car.add(Body(type="SportsCar"))

    def get_result(self):
        return self._car

class CarDirector:
    def __init__(self, builder: BuilderInterface):
        self.builder = builder

    def construct_car(self):
        self.builder.build_body()
        self.builder.build_engine()
        self.builder.build_transmission()

        return self.builder.get_result()