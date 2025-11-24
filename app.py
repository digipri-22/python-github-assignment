print("Welcome to my Python program!")
kitties = input("How many kitties do you have?")
try:
    kitties=int(kitties)
except ValueError:
    print("Please enter a valid number.")
    kitties = input("How many kitties do you have?")
    exit()
kittyFoodperDay=kitties*3
print(f"You need {kittyFoodperDay} servings of kitty food per day!")
