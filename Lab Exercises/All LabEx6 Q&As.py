"""Lab Exercise 6
Submitted by Tenzin Tsering Shrestha, 27C"""


def q1():
    """ to find out the sum of element of a list by using recursion"""

    def sumlist(lista):
        if not lista:
            return 0  # End of recursion
        else:
            return int(lista[0]) + sumlist(lista[1:])  # Recursion step

    print("Enter the values in the list, with spaces between each value:")
    temp = input()
    temp = temp.split()
    print(sumlist(temp))

def q2():
    """to display the multiplication of 3 upto n number using recursion"""

    def mult3(n):
        if n == 1:
            return 3
        else:
            return 3 + mult3(n-1)

    print("Enter the number of times to multiply 3")
    print(mult3(int(input())))


def q3():
    """returns the sum of first n integers"""

    def sumfirst(nint):
        if nint == 1:
            return 1
        else:
            return nint + sumfirst(nint-1)

    n = int(input("Enter the n number of integers:\n"))
    print(sumfirst(n))


def q4():
    """check if the given string is palindrome, else not palindrome"""

    def checkpal(string):
        if len(string) == 0:
            return True
        else:
            if string[0] == string[-1]:
                return checkpal(string[1:-1])
            else:
                return False

    a = str(input("Enter the string:\n"))
    if checkpal(a):
        print(f"The given string '{a}' is a palindrome.")
    else:
        print(f"The given string '{a}' is not a palindrome.")


def q5():
    """ check if the number is palindrome or not"""

    def checkpal(string):
        if len(string) == 0:
            return True
        else:
            if string[0] == string[-1]:
                return checkpal(string[1:-1])
            else:
                return False

    a = str(input("Enter the number:\n"))
    if checkpal(a):
        print(f"The given number '{a}' is a palindrome.")
    else:
        print(f"The given number '{a}' is not a palindrome.")


q5()
