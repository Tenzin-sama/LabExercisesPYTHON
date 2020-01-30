# Lab Exercise 2, Question 2

"""WAP which accepts marks of four subjects and
display total marks, percentage and grade."""

"""Hint: more than 70% –> distinction,                              
more than 60% –> first,d                                            
more than 40% –> pass,                                              
less than 40% –> fail"""

submark = [0, 0, 0, 0]
totmark = 0
status = "Pass"
grade = "Fail"
for n in range(4):
    print(f"Enter the marks of subject {n + 1}")
    submark[n] = int(input())
    totmark = totmark + submark[n]

# calculating percentage
floatper = (totmark / 400) * 100
per = str(floatper)
subper = per[0:2]
dig = per[2:5]
percentage = f"{subper}{dig}"

# check grade
if 0 <= floatper < 40:
    status = "Fail"
elif 40 <= floatper < 60:
    grade = "Pass"
elif 60 <= floatper < 70:
    grade = "First Division"
else:
    grade = "Distinction"
if status == "Pass":
    print("The student has passed the exam")
else:
    print("The student has failed the exam")
print(f"Total marks: {totmark}/400")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
print()
input()
