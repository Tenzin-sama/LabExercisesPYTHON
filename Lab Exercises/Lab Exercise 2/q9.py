# Lab Exercise 2, Question 9

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
input()
