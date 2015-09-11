#-------------------------------------------------------------------------------
# Name:        main
# Purpose:
#
# Author:      Lisa
#
# Created:     28/04/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Lookup import *
from Employee import *
from Airport import *
from Currency import *
from TravelAgent import *

import csv


# ----------- setting up the lookup details ------------------------------------
lookup = Lookup()
lookup.readEmployee('employees.csv')
lookup.readAirport()
lookup.readCountryCurrency()
lookup.readCurrencyRate()
agent = TravelAgent(lookup)

# ------------ Confirming that data is ready -----------------------------------
print('All csv data has been read.')
print('Total Employees:', len(lookup.employee_info))
print('Total Airports:', len(lookup.airport_info))
print('Total Currencies:', len(lookup.currency_info))
print('Total Exchange Rates:', len(lookup.currencyrate_info))

# ------------ Basic information retrieval exercises ---------------------------
print('Currency for LHR airport: ',lookup.getCurrency('LHR')) # GBP
print('Exchange Rate for GBP to EUR: ',lookup.getExchangeRate('LHR')) # 1.4029
print('Latitude and Longitude of LHR airport: ',lookup.getLatLong('LHR')) # (51.4775, -0.461389)
print('Distance in km from DUB to LHR: ', agent.costLeg('DUB','LHR'))

# ------------- Employee itinerary results -------------------------------------
alice = agent.lookup.employee_info.get('Alice')
aliceList = lookup.getCityList(alice)
aliceResult = agent.getResultByName('Alice')
print('''\nAlice is based in %s and this month she will travel to %s
The best price for her travel plan is: Euro %s, and the itinerary will be: %s '''
        % (aliceList[0], aliceList[1:-1], aliceResult[-1], aliceResult[1:-1]))

# ---------- get results for new employee (not in csv file already read) ---
georgia = ["Georgia","CDG","SIN","AMS","LAX","SYD"]
georgiaResult = agent.getIndividualResult(georgia)
print('''\nGeorgia has just joined the sales team.
She is based in %s and will travel to: %s
The best price for her travel plan is: Euro %s,
and the itinerary will be: %s \n'''
% (georgia[1], georgia[2:], georgiaResult[-1], georgiaResult[:-1]))



print('Be sure to check out the GUI !! Run gui.py to see it in action ')


##def runTheGUI():
##    import gui
##   gui.runGUI()
##
##runTheGUI()
