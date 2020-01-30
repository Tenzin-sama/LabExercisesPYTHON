# Lab Exercise 2, Question 5

"""For given integer x,
print ‘True’ if it is positive,
print ‘False’ if it is negative and
print ‘zero’ if it is 0"""

x = int(input("Enter a number: "))
if x > 0:
    status = "positive"
elif x < 0:
    status = "negative"
else:
    status = "zero"
print(f"Integer x ({x}) is  {status}")
print()
input()
