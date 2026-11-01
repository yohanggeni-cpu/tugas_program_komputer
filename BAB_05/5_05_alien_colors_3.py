# Exercise 5-5: Alien Colors #3

def shoot_alien(alien_color: str) -> None:
    """Berikan poin sesuai warna alien."""
    if alien_color == "green":
        points = 5
    elif alien_color == "yellow":
        points = 10
    elif alien_color == "red":
        points = 15
    else:
        print("Warna alien tidak dikenal.")
        return
    print(f"Alien {alien_color}: kamu memperoleh {points} poin.")


for color in ("green", "yellow", "red"):
    shoot_alien(color)
