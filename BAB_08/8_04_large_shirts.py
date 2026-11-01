# Exercise 8-4: Large Shirts

def make_shirt(size: str = "L", message: str = "I love Python") -> None:
    """Tampilkan detail kaus dengan nilai default."""
    print(f"Kaus ukuran {size.upper()} dengan tulisan: '{message}'.")


make_shirt()  # Large dengan pesan default.
make_shirt(size="M")  # Medium dengan pesan default.
make_shirt(size="S", message="UNS Industrial Engineering")
