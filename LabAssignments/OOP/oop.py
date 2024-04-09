"""
Lab - Object Oriented Programming (OOP)
By: Carson White

CSCI 110
Date: 4/9/2024

Object Oriented Programming:
Using user-defined class/type, program finds area and 
circumference of a circle.
"""

import math


class Circle(object):
    """
    Class that represents a circle with three attributes – radius, area and circumference.
    Class has two user-defined methods findArea and findCirumference and two special 
    built-in methods:   __init__ and __str__.
    """

    def __init__(self, r=0):
        self.radius = r
        self.area = self.findArea()
        self.circumference = self.findCircumference()

    def findArea(self):
        return math.pi*(self.radius**2)

    def findCircumference(self):
        # FIXME1-Fixed: Find and return the circumference of the circle (20 pts)
        return math.pi*(self.radius*2)

    def __str__(self):
         # FIXME2-Fixed: Modify the statement to return circumference as well (20 pts)
        return "Circle - radius: {:.2f}  area: {:.2f} and circumference: {:.2f}".format(self.radius, self.area, self.circumference)


def main():
    # instantiate aCir object with radius 1
    aCir = Circle(1)
    print(aCir)
    # FIXME3-Fixed: (20 pts)
    # Instantiate another circle with radius 5
    # Print the circle
    new_circ = Circle(5)
    print (new_circ)

    # FIMXE4-Fixed: (20 pts)
    # prompt user to enter radius and store into a variable
    print(" Please enter a radius.  ")
    radius = int(input())

    # FIXME5-Fixed: (20 pts)
    # create a circle with the user provided radius
    # print the circle
    new_circ2 = Circle(radius)
    print (new_circ2)


if __name__ == "__main__":
    main()