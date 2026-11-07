from restaurant import Restaurant

restaurant = Restaurant("Kantin Teknik", "Indonesia")
print("Awal:", restaurant.number_served)
restaurant.number_served = 25
restaurant.set_number_served(40)
restaurant.increment_number_served(15)
print("Pelanggan terlayani:", restaurant.number_served)
