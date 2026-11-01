# Exercise 8-3: T-Shirt

def make_shirt(size: str, message: str) -> None:
    """Tampilkan ringkasan ukuran dan tulisan pada kaus."""
    print(f"Kaus ukuran {size.upper()} dengan tulisan: '{message}'.")


make_shirt("M", "Belajar Python")  # Argumen positional.
make_shirt(size="L", message="Teknik Industri")  # Argumen keyword.
