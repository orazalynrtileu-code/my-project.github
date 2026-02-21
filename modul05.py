import threading
import json
import os
import copy
from abc import ABC, abstractmethod

class ConfigurationManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ConfigurationManager, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._settings = {}
        self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    def load_from_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError("Configuration file not found")
        with open(filepath, "r", encoding="utf-8") as f:
            self._settings = json.load(f)

    def save_to_file(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self._settings, f, indent=4)

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key):
        if key not in self._settings:
            raise KeyError(f"Setting '{key}' not found")
        return self._settings[key]


class Report:
    def __init__(self):
        self.header = ""
        self.content = ""
        self.footer = ""

    def __str__(self):
        return f"{self.header}\n{self.content}\n{self.footer}"


class IReportBuilder(ABC):
    @abstractmethod
    def set_header(self, header): pass

    @abstractmethod
    def set_content(self, content): pass

    @abstractmethod
    def set_footer(self, footer): pass

    @abstractmethod
    def get_report(self): pass


class TextReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = header

    def set_content(self, content):
        self.report.content = content

    def set_footer(self, footer):
        self.report.footer = footer

    def get_report(self):
        return self.report


class HtmlReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header):
        self.report.header = f"<h1>{header}</h1>"

    def set_content(self, content):
        self.report.content = f"<p>{content}</p>"

    def set_footer(self, footer):
        self.report.footer = f"<footer>{footer}</footer>"

    def get_report(self):
        return self.report


class ReportDirector:
    def construct_report(self, builder, header, content, footer):
        builder.set_header(header)
        builder.set_content(content)
        builder.set_footer(footer)
        return builder.get_report()


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def clone(self):
        return copy.deepcopy(self)


class Discount:
    def __init__(self, description, percent):
        self.description = description
        self.percent = percent

    def clone(self):
        return copy.deepcopy(self)


class Order:
    def __init__(self, products=None, delivery_cost=0.0, discounts=None, payment_method=""):
        self.products = products if products else []
        self.delivery_cost = delivery_cost
        self.discounts = discounts if discounts else []
        self.payment_method = payment_method

    def clone(self):
        cloned_products = [p.clone() for p in self.products]
        cloned_discounts = [d.clone() for d in self.discounts]
        return Order(cloned_products, self.delivery_cost, cloned_discounts, self.payment_method)

    def total_price(self):
        total = sum(p.price * p.quantity for p in self.products)
        for d in self.discounts:
            total -= total * (d.percent / 100)
        total += self.delivery_cost
        return total


def test_singleton(thread_id):
    config = ConfigurationManager.get_instance()
    print(f"Thread {thread_id} config id:", id(config))


if __name__ == "__main__":
    config1 = ConfigurationManager.get_instance()
    config1.set("app_name", "MyApp")
    config1.save_to_file("config.json")

    config2 = ConfigurationManager.get_instance()
    print("Same instance:", id(config1) == id(config2))
    print("App name:", config2.get("app_name"))

    threads = []
    for i in range(5):
        t = threading.Thread(target=test_singleton, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    director = ReportDirector()

    text_builder = TextReportBuilder()
    text_report = director.construct_report(text_builder, "Text Header", "Text Content", "Text Footer")
    print("\nText Report:")
    print(text_report)

    html_builder = HtmlReportBuilder()
    html_report = director.construct_report(html_builder, "HTML Header", "HTML Content", "HTML Footer")
    print("\nHTML Report:")
    print(html_report)

    product1 = Product("Laptop", 1000, 1)
    product2 = Product("Mouse", 50, 2)
    discount = Discount("Promo", 10)

    order1 = Order([product1, product2], 20, [discount], "Credit Card")
    order2 = order1.clone()
    order2.products[0].name = "Gaming Laptop"

    print("\nOriginal first product:", order1.products[0].name)
    print("Cloned first product:", order2.products[0].name)
    print("Original total:", order1.total_price())
    print("Cloned total:", order2.total_price())