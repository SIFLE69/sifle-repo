print("welcome to area calculator")


import math as mt

p = 3.14


a = ("enter the number after the satement what you wnat to do\narea of square(1)\narea of rectangle(2)\narea of triangle(3)\narea of circle(4)")
print(a)


s = input()


def sqr_area (sid):
     f = print(sid*sid)

def crcl_area (rad):
     d = print(p*rad**2)

def rect_area (x,y):
    s =print(x*y)

def tri_area (bas,hit):
     l = print(0.5*bas*hit)


if s == ("1"):
    sid = int(input("enter the side of square   "))
    sqr_area(sid)

if s == ("4"):
    rad = int(input("enter the radius of circle   "))
    crcl_area(rad)

if s == ("2"):
    x = int(input("enter the length   "))
    y = int(input("enter the breadth  "))
    rect_area(x,y)

if s == ("3"):
    bas = int(input("enter the base of triangle  "))
    hit = int(input("enter the height of triangle   "))
    tri_area (bas,hit)






