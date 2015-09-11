#-------------------------------------------------------------------------------
# Name:        Lookup
# Purpose:
#
# Author:      Lisa
#
# Created:     29/04/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv

from Employee import *
from Airport import *
from Currency import *


class Lookup:
    ''' Lookup class for the travel information '''
    def __init__(self):
        self.airport_info={}
        self.employee_info={}
        self.currency_info={}
        self.currencyrate_info={}

    def readEmployee(self, filename):
        ''' reads csv file and creates dictionary of employees '''
        with open(filename, encoding ="utf8", mode='rt') as infile:
            reader=csv.reader(infile)
            for row in reader:
                anemployee=Employee(row[0],(row[1]),row[2],row[3], row[4], row[5])
                self.employee_info[row[0]]=anemployee

    def readAirport(self):
        ''' reads csv file and creates dictionary of airports '''
        with open('airport.csv', encoding ="utf8", mode='rt') as infile:
            reader=csv.reader(infile)
            for row in reader:
                anairport=Airport(row[4], row[2], row[3],float(row[6]), float(row[7]))
                self.airport_info[row[4]]=anairport

    def readCountryCurrency(self):
        ''' reads csv file and creates dictionary of country currencies '''
        with open('countrycurrency.csv', encoding ="utf8", mode='rt') as infile:
            reader=csv.reader(infile)
            for row in reader:
                acurrency=Currency(row[17],(row[14]),row[0])
                self.currency_info[row[0]]=acurrency

    def readCurrencyRate(self):
        ''' reads csv file and creates dictionary of currency exchange rates '''
        with open('currencyrates.csv', encoding ="utf8", mode='rt') as infile:
            reader=csv.reader(infile)
            for row in reader:
                arate=CurrencyRate(row[0],(row[1]),float(row[2]))
                self.currencyrate_info[row[1]]=arate


# ------------ Methods for looking up info ------------------------------------

    def getCityList(self, employee):
        ''' returns list of employee travel cities with home at beginning and end. '''
        cityList = [employee.homecity,employee.visitcity1,employee.visitcity2, employee.visitcity3, employee.visitcity4,employee.homecity]
        return cityList

    def getCurrency(self,airportCode):
        ''' Look up currency code by airport code'''
        airport = self.airport_info.get(airportCode)
        country = airport.countryName
        currency = self.currency_info.get(country)
        currencyCode = currency.currencyCode
        return currencyCode

    def getExchangeRate(self,airportCode):
        ''' look up exchange rate by airport code'''
        currency = self.getCurrency(airportCode)
        rateobj = self.currencyrate_info.get(currency)
        rate = rateobj.rateToEuro
        return rate

        # -- not in use here, see agent
    def getLatLong(self,airportCode):
        '''look up latitude & longitude by airport code '''
        if airportCode.upper() in self.airport_info:
            airport = self.airport_info.get(airportCode.upper())
            latitude = airport.latitude
            longitude = airport.longitude
            return latitude,longitude
        else:
            raise ValueError('Invalid airport code: ', airportCode)



def main():
    lookup = Lookup()
    lookup.readEmployee('employees.csv')
    lookup.readAirport()
    lookup.readCountryCurrency()
    lookup.readCurrencyRate()

    print('Total Employees:', len(lookup.employee_info))
    print('Total Airports:', len(lookup.airport_info))
    print('Total Currencies:', len(lookup.currency_info))
    print('Total Rates:', len(lookup.currencyrate_info))

    print(lookup.getCurrency('LHR')) # GBP
    print(lookup.getExchangeRate('LHR')) # 1.4029
    print(lookup.getLatLong('DUB')) # (53.421333, -6.270075)

if __name__ == '__main__':
    main()