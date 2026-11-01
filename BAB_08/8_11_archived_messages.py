# Exercise 8-11: Archived Messages

def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    """Kirim salinan pesan sehingga daftar asli tetap utuh."""
    while messages:
        message = messages.pop(0)
        print(f"Mengirim: {message}")
        sent_messages.append(message)


messages = ["Halo!", "Semangat belajar.", "Sampai jumpa."]
sent_messages = []
send_messages(messages.copy(), sent_messages)
print("Daftar asli tetap:", messages)
print("Daftar terkirim:", sent_messages)
