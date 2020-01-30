# Lab Excersise 1, Question 6

"""find BMI using body mass and height"""

print("Enter the body mass (in kg): ")
mass = float(input())
print("Enter the height (in metres): ")
height = float(input())
bmi = mass / (height ** 2)
print(f"The BMI for given values is {bmi}")
print()
input()
