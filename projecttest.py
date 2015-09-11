#-------------------------------------------------------------------------------
# Name:        testingFlying
# Purpose:      Testing the individual functions and
#               broad functionality for success and failure
# Author:      Lisa
#
# Created:     01/05/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Lookup import *
from Employee import *
from Airport import *
from Currency import *
from TravelAgent import *

import unittest
import pytest

lookup = Lookup()
lookup.readEmployee('employees.csv')
lookup.readAirport()
lookup.readCountryCurrency()
lookup.readCurrencyRate()

agent = TravelAgent(lookup)


class FileReadToClasses(unittest.TestCase):
    ''' Tests that lookup is saving all data from csv files into objects '''

    def test_employees(self):
        employees = 4
        self.assertEqual(employees,len(lookup.employee_info.values()))

    def test_airports(self):
        airports = 5835
        self.assertEqual(airports,len(lookup.airport_info.values()))

    def test_currencies(self):
        currencies = 250
        self.assertEqual(currencies,len(lookup.currency_info.values()))

    def test_rate(self):
        rates = 196
        self.assertEqual(rates,len(lookup.currencyrate_info.values()))


class LookupInfo(unittest.TestCase):
    ''' Tests that lookup can retreive data from objects '''

    def test_employee_info(self):
        homeTom = 'LHR'
        tom = agent.lookup.employee_info.get('Tom')
        result = tom.homecity
        self.assertEqual(homeTom,result)

    def test_airport_info(self):
        cityDUB = 'Dublin'
        airport = agent.lookup.airport_info.get('DUB')
        result = airport.cityName
        self.assertEqual(cityDUB,result)

    def test_currency_info(self):
        currencyPoland = 'Zloty'
        country = agent.lookup.currency_info.get('Poland')
        result = country.currencyName
        self.assertEqual(currencyPoland,result)

    def test_rate_info(self):
        rateZloty = 0.2417
        rate = agent.lookup.currencyrate_info.get('PLN')
        result = rate.rateToEuro
        self.assertEqual(rateZloty,result)


class KnownDistances(unittest.TestCase):
    ''' Tests that distances are calculating correctly '''

    known_distances = ( ('JFK','AAL',5968.772393136871),
                        ('DUB','LHR',449.0331469073003),
                        ('AMS','AAL',624.1210779313353),
                        ('CDG','LHR',347.8486686404139) )

    def test_known_distances(self):
        for airport1,airport2,distance in self.known_distances:
            result = agent.calcDistanceBetweenAirports(airport1,airport2)
            self.assertEqual(distance,result)


class KnownLegCosts(unittest.TestCase):
    ''' Tests that leg costs are calculating correctly '''
    known_leg_costs = ( ('JFK','AAL',5663.17),
                        ('DUB','LHR',449.03),
                        ('AMS','AAL',624.12),
                        ('CDG','LHR',347.85) )

    def test_known_leg_costs(self):
        for airport1,airport2,legCost in self.known_leg_costs:
            result = agent.costLeg(airport1,airport2)
            self.assertEqual(legCost,result)


class KnownRouteCosts(unittest.TestCase):
    ''' Tests that route costs are calculating correctly '''

    known_route_costs = ((['DUB','JFK','AAL','CDG','SYD','DUB'],40344.48),
                        (['DUB', 'LHR', 'CDG', 'ARN', 'SIN', 'ARN', 'DUB'], 10303.59),
                        (['DUB', 'LHR', 'CDG', 'AMS', 'AAL', 'DUB'], 2106.56),
                        (['LHR', 'AMS', 'SIN', 'SFO', 'DUB', 'LHR'], 28524.54) )

    def test_known_routecost(self):
        for route,cost in self.known_route_costs:
            result = agent.costRoute(route)
            self.assertEqual(cost,result[-1])


class BestRoute(unittest.TestCase):
    ''' Tests that lowest cost possible route is returned for Best Route '''

    def test_best_Alice(self):
        bestAlice = ['Alice', 'DUB', 'CDG', 'AAL', 'SYD', 'JFK', 'DUB', 20431.58]
        result = agent.getResultByName('Alice')
        self.assertEqual(bestAlice,result, 'Best Route for Alice')


class BadInfo(unittest.TestCase):
    ''' Tests that bad data is recognised and flagged '''

    def test_empty_employeeName(self):
        self.assertRaises(ValueError,Employee,"","DUB","JFK","AAL","CDG","SYD")

    def test_nonStr_employeeName(self):
        self.assertRaises(TypeError,Employee,34,"DUB","JFK","AAL","CDG","SYD")

    def test_bad_airport(self):
        self.assertRaises(ValueError,lookup.getLatLong,'abc')


if __name__ == '__main__':
    unittest.main()
