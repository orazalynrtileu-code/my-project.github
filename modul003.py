from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []
        self.payment_method = None
        self.delivery_method = None

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def calculate_total(self, discount_calculator):
        total = sum(product.price * quantity for product, quantity in self.items)
        return discount_calculator.apply_discount(total)

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def set_delivery_method(self, delivery_method):
        self.delivery_method = delivery_method

    def checkout(self, notification_service):
        if self.payment_method:
            self.payment_method.process_payment(self.calculate_total(DiscountCalculator()))
        if self.delivery_method:
            self.delivery_method.deliver_order(self)
        notification_service.send_notification(f"Order processed with total: {self.calculate_total(DiscountCalculator())}")

class IPayment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(IPayment):
    def process_payment(self, amount):
        print(f"Payment of {amount} processed via Credit Card")

class PayPalPayment(IPayment):
    def process_payment(self, amount):
        print(f"Payment of {amount} processed via PayPal")

class BankTransferPayment(IPayment):
    def process_payment(self, amount):
        print(f"Payment of {amount} processed via Bank Transfer")

class IDelivery(ABC):
    @abstractmethod
    def deliver_order(self, order):
        pass

class CourierDelivery(IDelivery):
    def deliver_order(self, order):
        print("Order delivered by courier")

class PostDelivery(IDelivery):
    def deliver_order(self, order):
        print("Order delivered by post")

class PickUpPointDelivery(IDelivery):
    def deliver_order(self, order):
        print("Order ready for pickup at point")

class INotification(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotification(INotification):
    def send_notification(self, message):
        print("Email sent:", message)

class SmsNotification(INotification):
    def send_notification(self, message):
        print("SMS sent:", message)

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount

class TenPercentDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.9

class DiscountCalculator:
    def __init__(self, strategy=NoDiscount()):
        self.strategy = strategy

    def apply_discount(self, amount):
        return self.strategy.apply_discount(amount)

if __name__ == "__main__":
    order = Order()
    order.add_product(Product("Ticket", 100), 2)
    order.add_product(Product("Snack", 10), 3)

    order.set_payment_method(CreditCardPayment())
    order.set_delivery_method(CourierDelivery())

    notification_service = EmailNotification()
    order.checkout(notification_service)

    discount_calc = DiscountCalculator(TenPercentDiscount())
    print("Total with discount:", order.calculate_total(discount_calc))
