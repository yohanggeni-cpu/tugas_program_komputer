# Exercise 7-3: Multiples of Ten
try:
    number = int(input("Masukkan sebuah bilangan: "))
    if number % 10 == 0:
        print(f"{number} merupakan kelipatan 10.")
    else:
        print(f"{number} bukan kelipatan 10.")
except ValueError:
    print("Input harus berupa bilangan bulat.")
