import json
from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    id: str
    price: float
    qty: int
    customer_email: str

class OrderLoader:
    def load(self, json_path: str) -> List[dict]:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)

class OrderParser:
    def parse(self, raw_data: List[dict]) -> List[Order]:
        orders = []
        for item in raw_data:
            if "id" not in item or "price" not in item or "qty" not in item or "email" not in item:
                raise ValueError("Invalid order payload")
            if item["qty"] <= 0:
                raise ValueError("qty must be positive")
            orders.append(Order(
                id=item["id"],
                price=float(item["price"]),
                qty=int(item["qty"]),
                customer_email=item["email"]
            ))
        return orders

class OrderCalculator:
    def calculate_total(self, orders: List[Order]) -> float:
        return sum(o.price * o.qty for o in orders)

class OrderReportFormatter:
    def format(self, orders: List[Order], total: float) -> str:
        return f"Orders count: {len(orders)}\nTotal: {total:.2f}\n"

class EmailSender:
    def send(self, to: str, subject: str, body: str) -> None:
        print(f"[EMAIL to={to}] {subject}\n{body}")

class OrderReportService:
    def __init__(self, loader: OrderLoader, parser: OrderParser,
                 calculator: OrderCalculator, formatter: OrderReportFormatter,
                 sender: EmailSender):
        self.loader = loader
        self.parser = parser
        self.calculator = calculator
        self.formatter = formatter
        self.sender = sender

    def make_and_send_report(self, json_path: str) -> str:
        raw = self.loader.load(json_path)
        orders = self.parser.parse(raw)
        total = self.calculator.calculate_total(orders)
        report = self.formatter.format(orders, total)

        for o in orders:
            self.sender.send(o.customer_email, "Your order report", report)

        return report