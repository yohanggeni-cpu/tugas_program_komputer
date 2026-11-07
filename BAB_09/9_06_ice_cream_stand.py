from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, "ice cream")
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print(f"- {flavor}")

stand = IceCreamStand("Wisang Ice Cream", ["vanila", "cokelat", "stroberi"])
stand.describe_restaurant()
stand.display_flavors()
