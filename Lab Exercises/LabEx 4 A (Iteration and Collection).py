# Lab Exercise 4,  Iteration and collection( List, tuple, set, Dictionary)
# Submitted by Tenzin Tsering Shrestha, 27 C
import random


def ques1():
    """to find those numbers which are divisible by 7 and multiple of 5,
    between 1500 and 2700 (both included). """
    print()
    num = []
    for i in range(1500, 2700 + 1):
        if i % 7 == 0 and i % 5 == 0:
            num.append(i)
    print(f" The numbers between 1500 and 2700 ( both included) that are divisible by both 7 and 5 are:")
    print(num)
    print()


def ques2():
    print("Choose the conversion: ")
    print("    [c] for celsius to fahrenheit")
    print("    [f] for fahrenheit to celsius")
    ans = input()
    conv = 0
    cs = ""
    if ans == "c":
        ans = "Celsius"
    elif ans == "f":
        ans = "Fahrenheit"
    print(f"Enter your temperature in {ans}")
    temp = int(input())
    if ans == "Celsius":
        conv = temp * (9 / 5) + 32
        cs = "Fahrenheit"
    elif ans == "Fahrenheit":
        conv = (5 / 9) * (temp - 32)
        cs = "Celsius"
    print(f"{temp} ({ans}) is {conv} ({cs})")
    print()


def ques3():
    """Write a Python program to guess a number between 1 to 9. """
    rnum = random.randrange(10)
    ans = 11
    while ans != rnum:
        print("Enter your guessed number")
        ans = int(input())
    print(f"Well Guessed!")


def ques4():
    """make a right-pointed isoceles triangle pattern with maximun no. of * being 5"""
    for i in range(1, 5 + 1):
        for j in range(i):
            print("*", end="")
        print()
    for i in range(4, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


def ques5():
    """accepts a word from user and reverses it"""
    print("Enter the word to be reversed")
    word = input()
    rev = ""
    for i in word:
        rev = i + rev
    print(rev)


def ques6():
    """ count the number of even and odd numbers from a series of numbers"""
    print("Enter the series of numbers: ")
    snum = input()
    odd, even = 0, 0
    for i in snum:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"The number of odd numbers is {odd}")
    print(f"The number of even numbers is {even}")


def ques7():
    """print all the numbers from 0 to 6 except 3 and 6"""
    for i in range(7):
        if not i == 3 or i == 6:
            print(i)


def ques8():
    """display the Fibonacci series between 0 and 50"""
    disp = 0
    a = 1
    series = []
    while disp <= 50:
        series.append(disp)
        temp = disp
        disp = disp + a
        a = temp
    print(series)


def ques9():
    """find factorial of a number"""
    factr = []
    num = int(input("Enter the num to find its factorial: "))
    for i in range(1, num):
        if num % i == 0:
            factr.append(i)
    print(f"The factorials of {num} are {factr}")
    print()


def ques10():
    print("Enter the string:")
    ans = input()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "num", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    numlet, numdig = 0, 0
    for i in ans:
        if i in letters:
            numlet += 1
        elif i in digits:
            numdig += 1
    print(f"{numdig} letters, {numlet} digits")


ques1()
ques2()
ques3()
ques4()
ques5()
ques6()
ques7()
ques8()
ques9()
ques10()
