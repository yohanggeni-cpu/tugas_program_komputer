from restaurant import Restaurant

places = [
    Restaurant("Kantin Teknik", "Indonesia"),
    Restaurant("Warung Pasta", "Italia"),
    Restaurant("Sushi Corner", "Jepang"),
]
for place in places:
    place.describe_restaurant()
