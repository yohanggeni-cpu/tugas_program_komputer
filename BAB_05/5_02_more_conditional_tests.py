# Exercise 5-2: More Conditional Tests
language = "Python"
print("Equality:", language == "Python")
print("Inequality:", language != "Python")
print("lower() True:", language.lower() == "python")
print("lower() False:", language.lower() == "PYTHON")

age = 20
print("Age == 20:", age == 20)
print("Age != 20:", age != 20)
print("Age > 18:", age > 18)
print("Age < 18:", age < 18)
print("Age >= 20:", age >= 20)
print("Age <= 18:", age <= 18)
print("AND True:", age > 18 and age < 30)
print("AND False:", age > 18 and age < 20)
print("OR True:", age < 18 or age == 20)
print("OR False:", age < 18 or age > 30)

majors = ["Teknik Industri", "Informatika"]
print("In list:", "Teknik Industri" in majors)
print("Not in list:", "Kedokteran" not in majors)
print("Negative membership:", "Informatika" not in majors)
