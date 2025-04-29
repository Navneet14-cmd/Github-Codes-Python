import math
volume = lambda h,r: (1/3)*math.pi*math.pow(r,2)*h
radius=float(input("Enter the radius: "))
height=float(input("Enter the height: "))
volume_of_cone=volume(height,radius)
print(volume_of_cone)