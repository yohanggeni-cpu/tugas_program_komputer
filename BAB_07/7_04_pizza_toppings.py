# Exercise 7-4: Pizza Toppings
print("Masukkan topping pizza. Ketik 'quit' untuk selesai.")
while True:
    topping = input("Topping: ").strip()
    if topping.lower() == "quit":
        break
    if topping:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")
    else:
        print("Topping tidak boleh kosong.")
print("Pesanan topping selesai.")
