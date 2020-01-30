# Lab Excersise 1, Question 5

"""A school decided to replace the desks in three classrooms.
    # Each desk sits two students.
    # Given the number of students in each class,
    # print the smallest possible number of desks that can be purchased
    # The program should read three integers:
    # the number of students in each of the three classes, a, b and c respectively."""

"""In the first test there are three groups.
    The first group has 20 students and thus needs 10 desks.
    The second group has 21 students, so they can get by with no fewer than 11 desks.
    11 desks are also enough for the third group of 22 students.
    So, we need 32 desks in total"""

numstu = [0, 20, 0, 0]
desk = [0, 0, 0, 0]
# input of number of students and finding required desks
for n in range(1, 4):
    print("Enter the number of students in class", n)
    numstu[n] = int(input())
    desk[n] = numstu[n] // 2
    # if odd number of students
    if bool(numstu[n] % 2):
        desk[n] = desk[n] + 1
# display results
for n in range(1, 4):
    print(f"Class {n} needs {desk[n]} desks")
print("Total desks needed is", desk[1] + desk[2] + desk[3])
print()
input()
