class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model}: Қозғалтқыш іске қосылды."

    def stop_engine(self):
        return f"{self.brand} {self.model}: Қозғалтқыш өшірілді."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors, transmission):
        super().__init__(brand, model, year)
        self.doors = doors
        self.transmission = transmission

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, body_type, has_box):
        super().__init__(brand, model, year)
        self.body_type = body_type
        self.has_box = has_box

class Garage:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Гаражға '{self.name}' көлік қосылды: {vehicle}")

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            print(f"Гараждан '{self.name}' көлік өшірілді: {vehicle}")

class Fleet:
    def __init__(self):
        self.garages = []

    def add_garage(self, garage):
        self.garages.append(garage)
        print(f"Автопаркке жаңа гараж қосылды: {garage.name}")

    def remove_garage(self, garage):
        if garage in self.garages:
            self.garages.remove(garage)
            print(f"Автопарктен гараж өшірілді: {garage.name}")

    def find_vehicle(self, model_name):
        print(f"\n--- Иіздеу: '{model_name}' ---")
        for garage in self.garages:
            for vehicle in garage.vehicles:
                if vehicle.model == model_name:
                    return f"Табылды: {vehicle} (Орны: {garage.name})"
        return "Көлік табылмады."

car1 = Car("Toyota", "Camry", 2023, 4, "Automatic")
bike1 = Motorcycle("BMW", "S1000RR", 2022, "Sport", False)

garage_a = Garage("№1 Гараж")
garage_a.add_vehicle(car1)

garage_b = Garage("VIP Гараж")
garage_b.add_vehicle(bike1)

my_fleet = Fleet()
my_fleet.add_garage(garage_a)
my_fleet.add_garage(garage_b)

print(f"\nТест: {car1.start_engine()}")
print(f"Тест: {bike1.stop_engine()}")

print(my_fleet.find_vehicle("Camry"))

garage_a.remove_vehicle(car1)
my_fleet.remove_garage(garage_a)