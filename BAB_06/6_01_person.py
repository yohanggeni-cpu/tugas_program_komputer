# Exercise 6-1: Person
person = {
    "first_name": "Alya",
    "last_name": "Putri",
    "age": 20,
    "city": "Surakarta",
}
for key, value in person.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
