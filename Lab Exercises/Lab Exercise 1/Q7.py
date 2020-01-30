# Lab Excersise 1, Question 7

# You live 4 miles from university.
# The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
# How long will the bus journey take? Alternatively, you could run to university.
# You jog the first mile at 7mph;
# then run the next two at15mph;
# before jogging the last at 7mph again.
# Will this be quicker or slower than the bus?

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
input()
