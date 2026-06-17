from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self, text: str) -> None:
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass

class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str) -> None:
        pass

class Copiable(ABC):
    @abstractmethod
    def copy(self) -> None:
        pass

class SimplePrinter(Printable):
    def print(self, text: str) -> None:
        print(text)

class MultiFunctionMachine(Printable, Scannable, Faxable, Copiable):
    def print(self, text: str) -> None:
        print(f"Printing: {text}")

    def scan(self) -> str:
        return "Scanned content"

    def fax(self, number: str) -> None:
        print(f"Faxing to {number}")

    def copy(self) -> None:
        print("Copying...")