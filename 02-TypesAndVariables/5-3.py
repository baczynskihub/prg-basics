###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
cuboid_volume=a*b*c
cuboid_surface_area=2*(a*b+a*c+b*c)
print(f"cuboid volume: {cuboid_volume}")
print(f'cuboid surface area: {cuboid_surface_area}')