class User:
    def __init__(self, first_name, last_name, age=18):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, usia {self.age}")

    def greet_user(self):
        print(f"Halo, {self.first_name}!")
