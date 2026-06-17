from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class OrderPrototype(Prototype):
    def __init__(self):
        self.order_number = None
        self.products = []
        self.total_price = None

    def clone(self):
        order_proto = OrderPrototype()
        order_proto.order_number = self.order_number
        order_proto.products = self.products[:]
        order_proto.total_price = self.total_price
        return order_proto

class Order:
    def __init__(self, prototype: OrderPrototype):
        self.order_number = prototype.order_number
        self.products = prototype.products
        self.total_price = prototype.total_price