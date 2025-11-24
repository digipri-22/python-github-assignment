# python-github-assignment
# first python github assignment!
print("Welcome to my Python program!")
kitties = input("How many kitties do you have?") #getting user input
try:
    kitties=int(kitties)
except ValueError:
    print("Please enter a valid number.")
    kitties = input("How many kitties do you have?") #repeating the question after incorrect answer
    exit()
kittyFoodperDay=kitties*3 #3 servings per kitty per day
print(f"You need {kittyFoodperDay} servings of kitty food per day!") #output
