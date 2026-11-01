# Exercise 5-3: Alien Colors #1

def shoot_alien(alien_color: str) -> None:
    """Berikan poin hanya jika warna alien hijau."""
    if alien_color == "green":
        print("Kamu memperoleh 5 poin!")


print("Versi yang lolos:")
shoot_alien("green")
print("Versi yang tidak lolos (tidak ada output poin):")
shoot_alien("red")
