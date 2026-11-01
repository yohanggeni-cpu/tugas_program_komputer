# Exercise 4-11: My Pizzas, Your Pizzas
my_pizzas = ["margherita", "pepperoni", "mushroom"]
friend_pizzas = my_pizzas.copy()
my_pizzas.append("four cheese")
friend_pizzas.append("hawaiian")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
