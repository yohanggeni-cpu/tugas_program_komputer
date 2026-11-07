from random import choice

pool = list("ABCDEFGHIJ") + list(range(10))
winning_items = [choice(pool) for _ in range(4)]
print("Item pemenang:", winning_items)
print("Tiket dengan empat item yang sama memenangkan hadiah.")
