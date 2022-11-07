import math


def get_radius():
    try:
        rad = int(input("Please, enter the radius:\n"))
    except ValueError as e:
        print(f"The value of the radius is incorrect: {e}")
        rad = get_radius()

    return rad


radius = get_radius()

area = math.pi * math.pow(radius, 2)

print(f"The area is: {round(area, 2)}")
