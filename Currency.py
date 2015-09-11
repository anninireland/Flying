#-------------------------------------------------------------------------------
# Name:        Currency
# Purpose:
#
# Author:      Lisa
#
# Created:     29/04/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Currency:
    ''' Currency Class - objects hold details about country currencies '''
    def __init__(self, currencyName, currencyCode, countryName):
        self.currencyName=currencyName
        self.currencyCode=currencyCode
        self.countryName=countryName

class CurrencyRate:
    ''' CurrencyRate Class - objects hold details about currency exchange rates '''
    def __init__(self, currencyName, currencyCode, rateToEuro):
        self.currencyName=currencyName
        self.currencyCode=currencyCode
        self.rateToEuro=rateToEuro