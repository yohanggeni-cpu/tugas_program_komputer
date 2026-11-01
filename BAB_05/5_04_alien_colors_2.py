# Exercise 5-4: Alien Colors #2

def shoot_alien(alien_color: str) -> None:
    """Hitung poin berdasarkan kondisi hijau atau bukan hijau."""
    if alien_color == "green":
        print("Kamu memperoleh 5 poin karena menembak alien hijau.")
    else:
        print("Kamu memperoleh 10 poin.")


shoot_alien("green")  # Menguji blok if.
shoot_alien("yellow")  # Menguji blok else.
