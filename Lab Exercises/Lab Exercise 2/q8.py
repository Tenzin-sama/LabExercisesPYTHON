# Lab Exercise 2, Question 8

"""Given a three-digit number
Find the sum of its digits."""

print("Enter a three- digit number")
a = int(input())
# seperate number into digits
num = str(a)
x = num[0]
y = num[1]
z = num[2]
print(f"The sum of three digits {x}, {y}, and {z} is:")
print(x + y + z)
print()
input()

