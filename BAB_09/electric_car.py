class Car:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_range(self):
        ranges = {40: 150, 65: 225}
        print(f"Jarak tempuh sekitar {ranges.get(self.battery_size, 150)} mil.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
