from abc import ABC, abstractmethod

class Order:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


class PriceCalculator:
    def calculate_total_price(self, order):
        return order.quantity * order.price * 0.9


class PaymentProcessor:
    def process_payment(self, payment_details):
        print("Payment processed using:", payment_details)


class EmailNotifier:
    def send_confirmation(self, email):
        print("Confirmation email sent to:", email)


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary


class SalaryStrategy(ABC):
    @abstractmethod
    def calculate(self, employee):
        pass


class PermanentSalary(SalaryStrategy):
    def calculate(self, employee):
        return employee.base_salary * 1.2


class ContractSalary(SalaryStrategy):
    def calculate(self, employee):
        return employee.base_salary * 1.1


class InternSalary(SalaryStrategy):
    def calculate(self, employee):
        return employee.base_salary * 0.8


class SalaryCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_salary(self, employee):
        return self.strategy.calculate(employee)


class Printer(ABC):
    @abstractmethod
    def print(self, content):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, content):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, content):
        pass


class AllInOnePrinter(Printer, Scanner, Fax):
    def print(self, content):
        print("Printing:", content)

    def scan(self, content):
        print("Scanning:", content)

    def fax(self, content):
        print("Faxing:", content)


class BasicPrinter(Printer):
    def print(self, content):
        print("Printing:", content)


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(NotificationSender):
    def send(self, message):
        print("Email sent:", message)


class SmsSender(NotificationSender):
    def send(self, message):
        print("SMS sent:", message)


class NotificationService:
    def __init__(self, senders):
        self.senders = senders

    def send_notification(self, message):
        for sender in self.senders:
            sender.send(message)


if __name__ == "__main__":
    order = Order("Laptop", 2, 1000)
    calculator = PriceCalculator()
    print(calculator.calculate_total_price(order))

    payment = PaymentProcessor()
    payment.process_payment("Visa")

    email = EmailNotifier()
    email.send_confirmation("test@mail.com")

    employee = Employee("Ali", 1000)
    salary_calc = SalaryCalculator(PermanentSalary())
    print(salary_calc.calculate_salary(employee))

    printer = AllInOnePrinter()
    printer.print("Hello")
    printer.scan("Doc")
    printer.fax("Fax Doc")

    service = NotificationService([EmailSender(), SmsSender()])
    service.send_notification("Hello World")
