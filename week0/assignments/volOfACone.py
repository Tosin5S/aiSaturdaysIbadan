# assignment 3: use math.pi to calculate the volume of a cone

import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

radius = 3
height = 5
result = cone_volume(radius, height)
print(result)  # Output: 47.12388980384689

