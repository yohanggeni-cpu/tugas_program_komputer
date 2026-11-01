# Exercise 7-8: Deli
sandwich_orders = ["tuna", "pastrami", "egg salad", "chicken"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)
