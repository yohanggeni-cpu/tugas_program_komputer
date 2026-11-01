# Exercise 5-6: Stages of Life

def describe_stage(age: int) -> str:
    """Kembalikan tahap kehidupan berdasarkan usia."""
    if age < 0:
        return "Usia tidak boleh negatif."
    if age < 2:
        return "bayi"
    if age < 4:
        return "balita"
    if age < 13:
        return "anak-anak"
    if age < 20:
        return "remaja"
    if age < 65:
        return "dewasa"
    return "lanjut usia"


for age in (1, 3, 10, 17, 25, 70):
    print(f"Usia {age}: {describe_stage(age)}")
