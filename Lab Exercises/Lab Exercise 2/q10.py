# Lab Exercise 2, Question 10

"""sum of three given integers.
However, if two values are equal sum will be zero."""

print("Enter the first integer")
a = int(input())
print("Enter the second integer")
b = int(input())
print("Enter the third integer")
c = int(input())
if a == b or a == c or b == c:
    print(f"Sum is zero")
else:
    print(f"Sum is {a + b + c}")
print()
input()
