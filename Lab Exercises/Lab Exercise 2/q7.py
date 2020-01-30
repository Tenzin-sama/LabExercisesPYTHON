# Lab Exercise 2, Question 7

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
input()

