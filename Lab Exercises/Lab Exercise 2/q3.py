# Lab Exercise 2, Question 3

"""Check whether the user input number is even or odd
and display it to user."""

print("Enter a number")
num = int(input())
if bool(num % 2):
    print("The number is odd")
else:
    print("The number is even")
print()
input()
