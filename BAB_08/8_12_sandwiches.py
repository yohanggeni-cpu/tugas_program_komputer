# Exercise 8-12: Sandwiches

def make_sandwich(*items: str) -> None:
    """Tampilkan seluruh isi sandwich yang dipesan."""
    if not items:
        print("Sandwich tanpa isian tambahan.")
        return
    print("Sandwich dengan isian:")
    for item in items:
        print(f"- {item}")
    print()


make_sandwich("keju", "tomat")
make_sandwich("ayam", "selada", "mayones")
make_sandwich("telur", "keju", "tomat", "saus")
