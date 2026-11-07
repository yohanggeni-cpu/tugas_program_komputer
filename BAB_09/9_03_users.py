class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}; usia {self.age}; "
              f"{self.email}; {self.city}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang.")

users = [
    User("Yohanes", "Wisanggeni", 18, "yohanggeni@student.uns.ac", "Surakarta"),
    User("Christabel", "Andani", 19, "christabel@example.com", "Semarang"),
]
for user in users:
    user.describe_user()
    user.greet_user()
