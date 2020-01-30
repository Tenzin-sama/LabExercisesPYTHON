# Lab Exercise 4,  List
# Submitted by Tenzin Tsering Shrestha, 27 C
import random
def ques1(numlist):
    print("1)")
    """to sum all the items in a list"""
    sumn = 0
    for i in numlist:
        sumn += i
    print(f"Sum of all numbers in list is {sumn}")
    print()


def ques2(numlist):
    print("2)")
    """to multiplies all the items in a list"""
    prod = 1
    for i in numlist:
        prod *= i
    print(f"Product of all numbers in list is {prod}")
    print()


def ques3(numlist):
    print("3)")
    """to get the largest number from a list"""
    maxn = 0
    for i in numlist:
        if i >= maxn:
            maxn = i
    print(f"Largest number in the list is {maxn}")
    print()


def ques4(numlist):
    print("4)")
    """to get the smallest number from a list"""
    smaln = 0
    for i in numlist:
        if i <= smaln:
            smaln = i
    print(f"Smallest number in the list is {smaln}")
    print()


def ques5(numlist):
    print("5)")
    """to count the number of strings
    where the string length is 2 or more
    and the first and last character are same from a given list of strings"""
    cnt = 0
    for i in numlist:
        i = str(i)
        if len(i) > 1:
            if i[0] == i[-1]:
                cnt += 1
    print(f"The number of strings with len greater than 1, and same first and last characters are {cnt}")
    print()


def ques6(numlist):
    print("6)")
    """to check a list is empty or not"""
    if len(numlist) == 0:
        print("List is empty")
    else:
        print("List is not empty")
    print()


def ques7(numlist):
    print("7)")
    """ to clone or copy a list"""
    listb = numlist.copy()
    return listb


def ques8(numlist):
    print()
    print("8)")
    """to print a specified list after removing the 0th, 4th and 5th elements"""
    listb = numlist.copy()
    del listb[0]
    del listb[4-1]  # accounting for 1 item already removed
    del listb[5-2]  # accounting for 2 items already removed
    print(listb)
    print()


def ques9(numlist):
    print("9)")
    """to select an item randomly from a list"""
    x = random.randrange(len(numlist)+1)
    print(f"Random item from list is {numlist[5]}")


a = [1, 212, 1831, 12, 98, 76, 69, 353]
b = []
ques1(a)
ques2(a)
ques3(a)
ques4(a)
ques5(a)
ques6(b)
ques6(a)
print(ques7(a))
ques8(a)
ques9(a)
