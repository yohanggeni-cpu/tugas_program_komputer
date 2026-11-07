from random import choice

pool = list("ABCDEFGHIJ") + list(range(10))
my_ticket = ["A", 3, "K", 7]
attempts = 0
while True:
    drawn = [choice(pool) for _ in range(4)]
    attempts += 1
    if drawn == my_ticket:
        break
print("Tiket:", my_ticket)
print(f"Percobaan sampai menang: {attempts:,}")
