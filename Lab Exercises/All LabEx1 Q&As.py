# Lab Exercises 1, from LMS
# Submitted by Tenzin Tsering Shrestha, 27 C

def ques1():
    """Write a program that takes three numbers and prints their numsum.
    Every number is given on a separate line."""

    print("Enter the first number")
    numsum = int(input())
    print("Enter the second number")
    numsum = numsum + int(input())
    print("Enter the third number")
    numsum = numsum + int(input())
    print("The sum of the three numbers is:")
    print(numsum)
    print()


def ques2():
    """reads the length of the base and the height of a right-angled triangle
    Prints the area
    Every number is given on a separate line"""

    print("Enter the measurements of the right angled triangle")
    length = int(input("Length: "))
    height = int(input("Height: "))
    print("The area of the triangle is:")
    print(f"{length * height}sq unit")
    print()


def ques3():
    """N students take K apples and distribute them among each other evenly
    The remaining (the undivisible) part remains in the basket
    How many apples will each single student get?
    How many apples will remain in the basket?
    The program reads the numbers N and K
    It should print the two answers for the questions above"""

    n = int(input("Number of students: "))
    k = int(input("Number of apples: "))
    # after distributing them evenly
    remain = k % n
    each = k // n
    print(f"Each student gets {each} apples.")
    print(f"{remain} apples remain in the basket")
    print()


def ques4():
    """Given the integer N - the number of minutes that is passed since midnight
    how many hours and minutes are displayed on the 24h digital clock?
    The program should print two numbers:
    the number of hours (between 0 and 23) and
    the number of minutes (between 0 and 59)"""

    """For example, if N = 150, then 150 minutes have passed since midnight
    i.e. now is 2:30 am. So, the program should print 2:30."""

    n = int(input("Number of minutes past midnight: "))
    hours = n // 60
    minutes = n % 60
    print(f"{hours}:{minutes}")
    print()


def ques5():
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


def ques6():
    """find BMI using body mass and height"""

    print("Enter the body mass (in kg): ")
    mass = float(input())
    print("Enter the height (in metres): ")
    height = float(input())
    bmi = mass / (height ** 2)
    print(f"The BMI for given values is {bmi}")
    print()


def ques7():
    """You live 4 miles from university.
    The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
    How long will the bus journey take? Alternatively, you could run to university.
    You jog the first mile at 7mph;
    then run the next two at15mph;
    before jogging the last at 7mph again.
    Will this be quicker or slower than the bus?"""

    distance = 4

    class bus:
        speed = 25
        stops = 10
        stopdelay = 2

    class foot:
        # speed on foot each mile
        mile1 = 7
        mile2 = 15
        mile3 = 15
        mile4 = 7

    # for time taken by bus,
    bus.totaldelay = bus.stopdelay * bus.stops
    bus.traveltime = (distance / bus.speed) * 60
    bus.actualtime = bus.traveltime + bus.totaldelay  # total time taken

    # for time taken on foot,
    time = 1 / foot.mile1
    time = time + (1 / foot.mile2)
    time = time + (1 / foot.mile3)
    time = time + (1 / foot.mile4)
    foot.actualtime = time * 60  # total time taken

    if foot.actualtime > bus.actualtime:
        faster = "bus"
    else:
        faster = "foot"

    print(f" It takes {foot.actualtime} minutes on foot.")
    print(f" It takes {bus.actualtime} minutes on bus.")
    print(f"Therefore, it is faster on {faster}")
    print()


def ques8():
    """accept radius and find area"""

    radius = int(input("Enter the radius of the circle: "))
    print("The area of the given circle is", 3.14 * (radius ** 2), "sq units")
    print()


def ques9():
    """to find sum of the first n positive integers."""

    print("Of how many first positive integers do you want their sum of?")
    n = int(input())
    sumn = (n * (n + 1)) / 2
    print(f"The sum of first {n} positive integers is {sumn}")
    print()


def ques10():
    """to convert seconds to day, hour, minutes and seconds."""

    print("Enter the number of seconds: ")
    sec = int(input())
    remsec = sec
    days = remsec // (24 * 60 * 60)
    remsec = remsec % (24 * 60 * 60)
    hours = remsec // (60 * 60)
    remsec = remsec % (60 * 60)
    minutes = remsec // 60
    remsec = remsec % 60
    print(f"{sec} seconds is {days} days, {hours} hours, {minutes} minutes and {remsec} seconds")
    print()


# Main Body
print()
print("Question 1: ")
ques1()
print("Question 2: ")
ques2()
print("Question 3: ")
ques3()
print("Question 4: ")
ques4()
print("Question 5: ")
ques5()
print("Question 6: ")
ques6()
print("Question 7: ")
ques7()
print("Question 8: ")
ques8()
print("Question 9: ")
ques9()
print("Question 10: ")
ques10()

