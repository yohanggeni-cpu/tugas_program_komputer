# Exercise 8-14: Cars

def make_car(manufacturer: str, model: str, **car_info) -> dict:
    """Simpan pabrikan, model, dan informasi opsional tentang mobil."""
    car = {"manufacturer": manufacturer, "model": model}
    car.update(car_info)
    return car


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
