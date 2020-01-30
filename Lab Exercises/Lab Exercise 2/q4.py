# Lab Exercise 2, Question 4

"""Given three integers,
print the smallest one.
(Three integers should be user input)"""

num = [0, 0, 0]
# input of numbers in list num
for n in range(3):
    print("Enter the number")
    num[n] = int(input())
# loop to shuffle and rearrange the list in increasing order (smallest, bigger,...)
for n in range(2):
    if num[0] > num[1]:
        temp = num[0]
        num[0] = num[1]
        num[1] = temp
    if num[1] > num[2]:
        temp = num[1]
        num[1] = num[2]
        num[2] = temp
print(f"The smallest number is {num[0]}")
print()
input()
