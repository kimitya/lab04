import math
num_of_sides = int(input("number of sides: "))
length_of_side = int(input("the lenght of a side: "))
if num_of_sides == 3:
    area = length_of_side ** 2 * math.sqrt(3)/4
    print(f"the area of the polygon is: {area}")
elif num_of_sides == 4:
    area = length_of_side ** 2
    print(f"the area of the polygon is: {area}")
else:
    p = num_of_sides * length_of_side / 2
    apothem = math.sqrt(length_of_side ** 2 - (length_of_side/2) ** 2)
    print(f"the area of the polygon is: {p * apothem / 2}")