# Exercise 7-9: No Pastrami
sandwich_orders = [
    "tuna", "pastrami", "roast beef", "pastrami", "egg salad", "pastrami",
]
finished_sandwiches = []
print("Deli kehabisan pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Saya membuat sandwich {sandwich}.")
    finished_sandwiches.append(sandwich)
print("Sandwich selesai:", finished_sandwiches)
