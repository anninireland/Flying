#-------------------------------------------------------------------------------
# Name:        Employee
# Purpose:
#
# Author:      Lisa
#
# Created:     29/04/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Lookup import *

class Employee:
    ''' Employee Class - objects hold details about employees '''
    def __init__(self, name, homecity, visitcity1, visitcity2, visitcity3,visitcity4):
        self.name=name
        self.homecity=homecity
        self.visitcity1=visitcity1
        self.visitcity2=visitcity2
        self.visitcity3=visitcity3
        self.visitcity4=visitcity4
        self.possRoutes = None # this attribute is populated when routes are created
        self.bestRoute = None # this attribute is populated when best route is found


    # see 'Public instead of Private Attributes' at http://www.python-course.eu/python3_properties.php
    @property
    def name(self):
        return self.__name

    @name.setter  # Verifies that Name is a string and not empty
    def name(self, val):
        if type(val) is not str:
            raise TypeError('Employee name must be a string')
        elif val == '':
            raise ValueError('Employee name cannot be blank')
        else:
            self.__name=val


def main():
    newEmployee = Employee("Alice","DUB","JFK","AAL","CDG","SYD")
    print(newEmployee.name,newEmployee.homecity)
    newEmployee = Employee("123","DUB","JFK","AAL","CDG","SYD")
    print(newEmployee.name,newEmployee.homecity)
    newEmployee = Employee("A","DUB","JFK","AAL","CDG","SYD")
    print(newEmployee.name,newEmployee.homecity)
    newEmployee4 = Employee("","DUB","JFK","AAL","CDG","SYD")
    print(newEmployee4.name,newEmployee4.homecity)
    newEmployee5 = Employee(34,"DUB","JFK","AAL","CDG","SYD")
    print(newEmployee5.name,newEmployee.homecity)

if __name__ == '__main__':
    main()
