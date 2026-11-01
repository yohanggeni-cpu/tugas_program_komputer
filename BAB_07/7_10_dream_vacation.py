# Exercise 7-10: Dream Vacation
responses = {}
print("Polling: Jika dapat mengunjungi satu tempat di dunia, ke mana")
print("Anda ingin pergi?")
while True:
    name = input("Nama (ketik 'quit' untuk selesai): ").strip()
    if name.lower() == "quit":
        break
    if not name:
        print("Nama tidak boleh kosong.")
        continue
    destination = input("Destinasi impian: ").strip()
    if destination:
        responses[name] = destination
    else:
        print("Destinasi tidak boleh kosong; respons tidak disimpan.")

print("\n--- Hasil Polling ---")
if responses:
    for name, destination in responses.items():
        print(f"{name} ingin mengunjungi {destination}.")
else:
    print("Belum ada respons.")
