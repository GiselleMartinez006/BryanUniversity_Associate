# The math.py file should ask a user the radius of the circle
# In the math.py file, write a code that calculate area of the circle.


# radius = r 
# a = area of circle
# a = pi times r to the power of 2

pi = 3.14

r = int(input('What is the radius of your circle in cm? '))
# print(r)
# print(r ** 2)
a = pi * (r ** 2)
print(f"The area of your circle is: {a} squared centimeters.")