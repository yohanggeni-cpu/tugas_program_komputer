# Exercise 8-9: Messages

def show_messages(messages: list[str]) -> None:
    """Cetak setiap pesan pada daftar."""
    for message in messages:
        print(message)


messages = ["Halo!", "Semangat belajar.", "Sampai jumpa."]
show_messages(messages)
