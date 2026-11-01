# Exercise 8-10: Sending Messages

def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    """Cetak pesan dan pindahkan dari daftar antrean ke daftar terkirim."""
    while messages:
        message = messages.pop(0)
        print(f"Mengirim: {message}")
        sent_messages.append(message)


messages = ["Halo!", "Semangat belajar.", "Sampai jumpa."]
sent_messages = []
send_messages(messages, sent_messages)
print("Daftar pesan tersisa:", messages)
print("Daftar pesan terkirim:", sent_messages)
