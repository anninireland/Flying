#-------------------------------------------------------------------------------
# Name:        Airport
# Purpose:
#
# Author:      Lisa
#
# Created:     29/04/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Airport:
    ''' Airport Class - objects hold details about airports '''
    def __init__(self, airportCode, cityName, countryName, latitude, longitude):
        self.airportCode=airportCode
        self.cityName=cityName
        self.countryName=countryName
        self.latitude=latitude
        self.longitude=longitude
