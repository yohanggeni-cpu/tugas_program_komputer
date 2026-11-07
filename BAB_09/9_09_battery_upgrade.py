from electric_car import ElectricCar

car = ElectricCar("Nissan", "Leaf", 2024)
print(car.get_descriptive_name())
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()
