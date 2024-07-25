import math as mt


print("Enter the given perimeters//n if not given pleasse enter 000")

a = int(input("enter length of side a "))

b =  int(input("enter length of side a "))

c =  int(input("enter length of side a "))

base = int(input("enter the base of the triangle "))

height = int(input("enter the length of height of the triangle "))

perimeter = int(input("enter the perimeter of the triangle "))

if (perimeter or a or b or c=='000'):
    print ("area of triangle is",0.5*base*height)

elif a==b==c:
    print(mt.sqrt(3)/4*a**2)

else:
    s = (perimeter/2)
    l = (s-a)*(s-b)*(s-c)
    print("area equal to ",s*mt.sqrt(s*l))
