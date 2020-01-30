# Lab Exercises 2, from LMS
# Submitted by Tenzin Tsering Shrestha, 27 C

def q1():
    """Lab Exercise 2, Question 1
    Check whether 5 is in list of first 5 natural numbers or not.
    Hint: List => [1,2,3,4,5]"""

    natnum = [1, 2, 3, 4, 5]
    if 5 in natnum:
        print("5 is in the list of first five natural numbers")
    else:
        print("5 is not in the list of first five natural numbers")
    print()


def q2():
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


def q3():
    """Check whether the user input number is even or odd
    and display it to user."""

    print("Enter a number")
    num = int(input())
    if bool(num % 2):
        print("The number is odd")
    else:
        print("The number is even")
    print()


def q4():
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


def q5():
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


def q6():
    """Given an integer number,
    print its last digit"""

    num = input("Enter a number: ")
    print(f"The last digit is {num[-1]}")
    print()


def q7():
    """Given a positive real number, print its fractional part."""

    print("Enter a number")
    num = float(input())

    # seperating into integer and decimal values
    strb = str(num)
    # spliting num and integerval in list format eg: 23.54 = [23, 54] as string
    temp = strb.split(".")
    # value after decimal point
    decimal = int(temp[1])  # value of decimal as integer
    power = 10 ** (len(str(decimal)))  # power multiple of 10^length of decimal, also denominator
    div = 2  # common divisor for numerator and denominator
    tempn = num * power
    tempm = power
    # loop to convert to smallest fraction
    while not div == 6:
        if (tempn / div) == (tempn // div) and (tempm / div) == (tempm // div):
            tempn = tempn / div
            tempm = tempm / div
        else:
            div += 1
    print(f"Fraction form: {int(tempn)}/{int(tempm)}")
    print()


def q8():
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


def q9():
    """Check whether the given year is leap year or not.
    # If year is leap print ‘LEAP YEAR’
    # else print ‘COMMON YEAR’"""

    """Hint:
    • a year is a leap year if its number is exactly divisible by 4
    and is not exactly divisible by 100
    • a year is always a leap year if its number is exactly divisible by 400"""

    print("Enter the year")
    year = int(input())
    # finding remainders
    rem4 = year % 4
    rem100 = year % 100
    rem400 = year % 400
    if rem4 == 0 and rem100 != 0:  # if divisible by 4 but not 100
        print("LEAP YEAR")
    elif rem400 == 0:  # if divisible by 400
        print("Leap Year")
    else:
        print("COMMON YEAR")
    print()

def q10():
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


def q11():
    """What is the result of 10**3?"""

    print("The result of 10**3 is: ")
    print(10 ** 3)
    print()


def q12():
    """Given x = 5,
    what will be the value of x after
    we run x+=3?"""

    x = 5
    x += 3
    print("The value of x (5) after we run x+=3 will be: ")
    print("8")
    print(f"Correct answer: {x}")
    print()


def q13():
    """What is the output of ‘APPLE’ > ‘apple’?"""

    print("Question 13")
    print("Output of ‘APPLE’ > ‘apple’ will be: ")
    print("False, because unicode of 'apple' is greater")
    a = "APPLE"
    b = "apple"
    print(f"Correct answer {a > b}")  # comparison of unicode
    print()


def q14():
    """What is the result of float (1)?"""

    print("Question 14")
    print("Result of float (1) is: ")
    print("1.0")
    print(f"Correct answer {float(1)}")
    print()


def q15():
    """What will be the output of the following if
    a =2, b=3, c =4, d = 3?"""

    print("Question 15")
    a = 2
    b = 3
    c = 4
    d = 3
    print(f" a = {a}, b = {b}, c = {c}, d = {d}")
    print()
    # ques (a)
    print("a) a==b: ")
    print("False")
    print(f"Correct answer {a == b}")
    print()
    # ques (b)
    print("b) a != d: ")
    print("True")
    print(f"Correct answer {a != d}")
    print()
    # ques (c)
    print("c) b == d: ")
    print("True")
    print(f"Correct answer {b == d}")
    print()
    # ques (d)
    print("d) a != c: ")
    print("True")
    print(f"Correct answer {a != c}")
    print()
    # ques (e)
    print("e) a += c: ")
    print("6")
    a += c
    print(f"Correct answer {a}")
    print()
    # ques (f)
    print("f) b /= d: ")
    print("1")
    b /= d
    print(f"Correct answer {b}")
    print()
    # ques (g)
    print("g) b > a: ")
    print("True")
    print(f"Correct answer {b > a}")
    print()
    # ques (h)
    print("h) a < d: ")
    print("False")
    print(f"Correct answer {a < d}")
    print()
    # ques (i)
    print("i) b-a == c-b: ")
    print("True")
    print(f"Correct answer {b - a == c - b}")
    print()
    # ques (j)
    print("j) b >= d: ")
    print("True")
    print(f"Correct answer {b >= d}")
    print()


# Main Body
print()
print("Question 1: ")
q1()
print("Question 2: ")
q2()
print("Question 3: ")
q3()
print("Question 4: ")
q4()
print("Question 5: ")
q5()
print("Question 6: ")
q6()
print("Question 7: ")
q7()
print("Question 8: ")
q8()
print("Question 9: ")
q9()
print("Question 10: ")
q10()
print("Question 11: ")
q11()
print("Question 12: ")
q12()
print("Question 13: ")
q13()
print("Question 14: ")
q14()
print("Question 15: ")
q15()
