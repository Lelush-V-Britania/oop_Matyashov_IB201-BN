from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Order:
    total: float

@dataclass
class Customer:
    kind: str

class Discount(ABC):
    @abstractmethod
    def apply(self, order: Order) -> float:
        pass

class RegularDiscount(Discount):
    def apply(self, order: Order) -> float:
        return order.total

class VipDiscount(Discount):
    def apply(self, order: Order) -> float:
        return order.total * 0.9

class EmployeeDiscount(Discount):
    def apply(self, order: Order) -> float:
        return order.total * 0.8

class BlackFridayDiscount(Discount):
    def apply(self, order: Order) -> float:
        return order.total * 0.5

def apply_discount(order: Order, discount_strategy: Discount) -> float:
    return discount_strategy.apply(order)