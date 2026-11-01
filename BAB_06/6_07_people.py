# Exercise 6-7: People
person_one = {
    "first_name": "Alya", "last_name": "Putri",
    "age": 20, "city": "Surakarta",
}
person_two = {
    "first_name": "Bima", "last_name": "Pratama",
    "age": 21, "city": "Semarang",
}
person_three = {
    "first_name": "Citra", "last_name": "Lestari",
    "age": 19, "city": "Yogyakarta",
}
people = [person_one, person_two, person_three]
for person in people:
    print("\nInformasi orang:")
    for key, value in person.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
