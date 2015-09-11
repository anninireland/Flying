#-------------------------------------------------------------------------------
# Name:        TravelAgent
# Purpose:      Travel Agent Class is a helper class responsible
#                   performing core functionality of the program
# Author:      Lisa
#
# Created:     29/04/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Lookup import *
from Employee import *
from gui import *

from itertools import permutations
from math import pi,sin,cos,acos,radians

class TravelAgent:
    ''' Travel Agent looks up and calculates information needed '''

    def __init__(self,TravelLookup):
        ''' creates a copy of the lookup resources for the travel agent '''
        self.lookup = TravelLookup

# -------- Methods for Travel Agent Tasks --------------------------------------

    def findPossibleRoutes(self, employee):
        ''' creates a list of all possible itineraries '''
        airports = self.lookup.getCityList(employee)
        itins = []

        # creates permutations of the visit cities with homecity at beginning and end
        for x in permutations(airports[1:-1]):
            itin = airports[:1] + list(x) + airports[-1:]
            itins.append(itin)

        # optional added stop feature
        # adds in each of the visit cities in each of the possible positions
        for c in range(len(itins)):
            combo=itins[c]
            for e in airports[0:4]:
                for i in range(5,0,-1):
                    newcombo=combo[:]
                    newcombo.insert(i,e)
                    itins.append(newcombo)

        # saves the possible routes to the employee object
        employee.possRoutes = itins
        return itins


    def calcDistanceBetweenAirports(self, airport1,airport2):
        ''' calculates the distance between 2 airports '''

        aircoords1 = self.lookup.getLatLong(airport1)
        aircoords2 = self.lookup.getLatLong(airport2)
        lat1, lat2, long1, long2 = float(aircoords1[1]),float(aircoords2[1]),(90.0-float(aircoords1[0])),(90.0-float(aircoords2[0]))

        # call calcDist
        distanceByAir=self.calcDist(lat1,long1,lat2,long2)
        return distanceByAir

    def calcDist(self,lat1,long1,lat2,long2):
        ''' calculates distance between 2 points '''
        rEarth = 6373.0
        radtheta1,radphi1,radtheta2,radphi2 = radians(lat1),radians(long1),radians(lat2),radians(long2)
        mycos=(sin(radphi1)*sin(radphi2)*cos(radtheta1 - radtheta2) + cos(radphi1)*cos(radphi2))
        distance=(acos(mycos))*rEarth
        return distance

    def costLeg(self, airport1,airport2):
        ''' calculates the cost of a flight from airport1 to airport2 '''
        ''' cost is based on specified calulation: cost = distance * exchangerate '''
        distance = self.calcDistanceBetweenAirports(airport1,airport2)
        rate = self.lookup.getExchangeRate(airport1)
        cost = round(rate * distance,2)
        return cost

    def costRoute(self, route):
        ''' calculates the cost of a route by repeatedly calling costLeg '''
        legstart = 0
        cost = 0
        while legstart < len(route)-1:
            legend = legstart + 1
            cost += self.costLeg(route[legstart],route[legend])
            legstart += 1
        # total cost is appended to the route list
        route.append(round(cost,2))
        return route

    def findAllCosts(self,possRoutes):
        ''' finds and records all costs for all routes passed in by calling costRoute for each '''
        for route in possRoutes:
            costThis = self.costRoute(route)
        return possRoutes

    def findBestRoute(self,possRoutes):
        ''' selects cheapest route from all route costs '''
        bestRoute = None
        costs = []
        for route in possRoutes:
            costs.append(route[-1])

        lowcost = min(costs)
        for route in possRoutes:
            if route[-1] == lowcost:
                bestRoute = route
                break
        return bestRoute

# ----------- GUI Methods ------------------------------------------------------
    def getIndividualResult(self,employeeInfo):
        ''' finds best route for one employee. Called when individual details submitted in GUI.
        Creates employee object and calculates best route. Returns result to GUI '''
        guiEmployee = Employee(employeeInfo[0],(employeeInfo[1]),employeeInfo[2],employeeInfo[3], employeeInfo[4], employeeInfo[5])
        guiPossRoutes = self.findPossibleRoutes(guiEmployee)
        guiAllCosts = self.findAllCosts(guiPossRoutes)
        guiBestRoute = self.findBestRoute(guiAllCosts)
        return guiBestRoute

# TODO ::  add getResultByName to GUI options
    def getResultByName(self,employeeName):
        ''' Finds best result for the given employee name. Returns error if name not found. '''
        self.lookup.readEmployee('employees.csv')

        if employeeName in self.lookup.employee_info:
            employee = self.lookup.employee_info.get(employeeName)
            employee.possRoutes = self.findPossibleRoutes(employee)
            allCosts = self.findAllCosts(employee.possRoutes)
            bestRoute = self.findBestRoute(employee.possRoutes)
            bestRoute.insert(0,employee.name)
            employee.bestRoute = bestRoute
        else:
            raise Exception(employee, 'not found')
        return employee.bestRoute

    def getBatchResult(self,inputFile,outputFile):
        ''' finds best routes for all in file. called when filename sent from GUI. '''

        # call to read csv of employees and create employee objects
        self.lookup.readEmployee(inputFile)

        # get best route for each employee
        for employee in self.lookup.employee_info.values():
            employee.possRoutes = self.findPossibleRoutes(employee)
            allCosts = self.findAllCosts(employee.possRoutes)
            bestRoute = self.findBestRoute(employee.possRoutes)
            bestRoute.insert(0,employee.name)
            employee.bestRoute = bestRoute

            # write result to output file
            with open(outputFile, encoding='utf8',mode='a') as resultsFile:
                writer = csv.writer(resultsFile)
                writer.writerow(bestRoute)
        return outputFile


def main():
    lookup = Lookup()
    lookup.readEmployee('employees.csv')
    lookup.readAirport()
    lookup.readCountryCurrency()
    lookup.readCurrencyRate()
    agent = TravelAgent(lookup)
    print(agent.costLeg('LAX','DUB'))
    result = agent.findBestRoute(agent.findPossibleRoutes(Employee("Alice","DUB","JFK","AAL","CDG","SYD")))
    print(result)
    print(agent.getResultByName('Tom'))

if __name__ == '__main__':
    main()