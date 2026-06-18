
print(" Welcome to the Interactive Personal Data Collector ")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

print("Thank you! Here is the information we collected:")

current_year = 2026
birth_year = current_year - age
height_cm =height = 100

print("Name:", name)
print("Type:", type(name))
print("Memory Address:", id(name))


print("Age:", age)
print("Type:", type(age))
print("Memory Address:", id(age))

print("Favourite Number:", favourite_number)
print("Type:", type(favourite_number))
print("Memory Address:", id(favourite_number))

print("birth_year :", birth_year )
print("type:", type ( birth_year))
print("Memory Address:", id(birth_year))


print("Thank you for using the Personal Data Collector.")

