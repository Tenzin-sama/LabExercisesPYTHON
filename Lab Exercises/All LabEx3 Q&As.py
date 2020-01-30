# Lab Exercise 3
# Submitted by Tenzin Tsering Shrestha, 27 C

"""Q.No.1"""
"""to find the Max of three numbers """


def maxnum(a, b, c):
    if a >= b and a >= c:
        mnum = a
    elif b >= a and b >= c:
        mnum = b
    else:
        mnum = c
    print(f"Maximum number is {mnum}")
    print()


"""Q.No.2"""
"""Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number."""


def fizz_buzz(a):
    rem3 = a % 3
    rem5 = a % 5
    if rem3 == 0 and rem5 == 1:
        toret = "Fizz"
    elif rem3 == 1 and rem5 == 0:
        toret = "Buzz"
    elif rem3 == 0 and rem5 == 0:
        toret = "FizzBuzz"
    else:
        toret = a
    print()
    return toret


""" Q.No.3"""
"""Write a function called showNumbers that takes a parameter called limit.
It should print all the numbers between 0 and limit,
with a label to identify the even and odd numbers."""


def shownumbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            print(i, "Even")
        else:
            print(i, "Odd")
    print()


"""Q.No.4"""
"""Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). """


def summult(limit):
    summ = 0
    for i in range(limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            summ = summ + i
    print()
    return summ


"""Q.No.5"""
"""Write a function showstars(rows) to display a line of "*"
with an extra * each row
with parameter row to determine the number of rows of stars"""


def showstars(rows):
    star = ""
    for i in range(rows):
        star = star + "*"
        print(star)
    print()


"""Q.No.6"""
"to reverse a string"


def revstr(string):
    rev = ""
    for i in range(len(string) - 1, -1, -1):
        rev = rev + string[i]
    print(f"Reverse of '{string}' is '{rev}'")
    print()


"""Q.No.7"""
""" accepts a string and calculate the number of upper case letters and lower case letters"""


def calcase():
    print("Enter the string to find no. of upper and lower case characters: ")
    string = input()
    upcnt = 0
    lowcnt = 0
    for i in range(len(string)):
        if string[i].isupper():
            upcnt += 1
        elif string[i].islower():
            lowcnt += 1
    print(f"There are {upcnt} upper-case characters.")
    print(f"There are {lowcnt} lower-case characters.")
    print()


"""Q.No.8"""
"""takes a number as a parameter and check the number is prime or not"""


def checkprm(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f" {num} is not a prime number.")
    print()


"""Q.No.9a"""
"""Check if passed string is palindrome or not"""


def checkpal(string):
    rev = reversed(string)
    if string == rev:
        print(f"The string '{string}' is a palindrome")
    else:
        print(f"The string '{string}' is not a palindrome")
    print()


"""Q.No.9b"""
"""Accept string from the user and display only those characters which are present at an even index"""


def evenindx(string):
    print(f"The characters in the even index of {string}are: ")
    for i in range(0, len(string) + 1, 2):
        print(string[i])
    print()


"""Q.No.10"""
""" find the factorial of a number using functions"""


def factorial(num):
    factr = []
    for i in range(1, num):
        if num % i == 0:
            factr.append(i)
    print(f"The factorials of {num} are {factr}")
    print()


# Main Body
print("Question 1:")
maxnum(34, 45, 36)
print("Question 2:")
print(fizz_buzz(24))
print("Question 3:")
shownumbers(9)
print("Question 4:")
print(summult(20))
print("Question 5:")
showstars(5)
print("Question 6:")
revstr("Hello World")
print("Question 7:")
calcase()
print("Question 8:")
checkprm(50)
print("Question 9a:")
checkpal("nurses")
print("Question 9b:")
evenindx("Information")
print("Question 10:")
factorial(8)
input("End of assignment: Lab Exercise 3")
