# Lab Excersise 1, Question 10


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
input()

