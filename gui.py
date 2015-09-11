#-------------------------------------------------------------------------------
# Name:        GUI manager
# Purpose:
#
# Author:      Lisa
#
# Created:     03/05/2015
# Copyright:   (c) Lisa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Lookup import *
from Employee import *
from Airport import *
from Currency import *
from TravelAgent import *

import csv

import tkinter


class simpleapp_tk(tkinter.Tk):
    ''' base GUI class '''
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        ''' set up GUI features '''
        self.grid() # initialize grid for positioning

# --- Labels for entry fields --- #
        # Main label
        self.mainLabelVariable = tkinter.StringVar() # create label variable
        mainLabel = tkinter.Label(self,textvariable=self.mainLabelVariable,anchor='center', fg='white',bg='slate grey')
        mainLabel.grid(column=0,row=0,columnspan=5,sticky='EW',padx=5,pady=5)
        self.mainLabelVariable.set("Welcome to the SuperSales Travel Calculator") # default text for label

        # Individual header label
        self.individualLabelVariable = tkinter.StringVar()
        individualLabel = tkinter.Label(self,textvariable=self.individualLabelVariable,anchor='w',fg='black',bg='sky blue')
        individualLabel.grid(column=0,row=1,columnspan=5,sticky='EW',padx=5,pady=5)
        self.individualLabelVariable.set("Individual Travel Calculation")

        # Individual Name label
        self.nameLabelVariable = tkinter.StringVar()
        nameLabel = tkinter.Label(self,textvariable=self.nameLabelVariable,anchor='w')
        nameLabel.grid(column=0,row=2,columnspan=1,sticky='EW',padx=5,pady=5)
        self.nameLabelVariable.set("Salesperson Name: ")

        # Individual Home label
        self.homeLabelVariable = tkinter.StringVar()
        homeLabel = tkinter.Label(self,textvariable=self.homeLabelVariable,anchor='w')
        homeLabel.grid(column=0,row=3,columnspan=1,sticky='EW',padx=5,pady=5)
        self.homeLabelVariable.set("Home Airport: ")

        # Individual Travel label
        self.travelLabelVariable = tkinter.StringVar()
        travelLabel = tkinter.Label(self,textvariable=self.travelLabelVariable,anchor='w')
        travelLabel.grid(column=0,row=4,columnspan=1,sticky='EW',padx=5,pady=5)
        self.travelLabelVariable.set("Travel Airports: ")

        # Batch header label
        self.batchLabelVariable = tkinter.StringVar()
        batchLabel = tkinter.Label(self,textvariable=self.batchLabelVariable,anchor='w',fg='black',bg='dark sea green')
        batchLabel.grid(column=0,row=8,columnspan=5,sticky='EW',padx=5,pady=5)
        self.batchLabelVariable.set("Batch Processing") # default text for label

        # Batch input filename label
        self.inputFileLabelVariable = tkinter.StringVar()
        inputFileLabel = tkinter.Label(self,textvariable=self.inputFileLabelVariable,anchor='w')
        inputFileLabel.grid(column=0,row=9,sticky='EW',padx=5,pady=5)
        self.inputFileLabelVariable.set("Enter the filename to upload: ") # default text for label

        # Batch output filename label
        self.outputFileLabelVariable = tkinter.StringVar()
        outputFileLabel = tkinter.Label(self,textvariable=self.outputFileLabelVariable,anchor='w')
        outputFileLabel.grid(column=0,row=10,sticky='EW',padx=5,pady=5)
        self.outputFileLabelVariable.set("Enter a filename for the results: ")

# --- Labels for displaying Results --- #

        # Individual Travel label - results
        self.individualResultsVariable = tkinter.StringVar()
        individualResults = tkinter.Label(self,textvariable=self.individualResultsVariable,anchor='w',fg='navy')
        individualResults.grid(column=0,row=7,columnspan=5,sticky='EW',padx=5,pady=5)

        # Batch results label
        self.batchResultsLabelVariable = tkinter.StringVar()
        batchResultsLabel = tkinter.Label(self,textvariable=self.batchResultsLabelVariable,anchor='w')
        batchResultsLabel.grid(column=0,row=11,columnspan=5,sticky='EW',padx=5,pady=5)

# --- Labels for displaying reminders/alerts --- #

        # Airport Code reminder label
        self.aircodeLabelVariable = tkinter.StringVar()
        aircodeLabel = tkinter.Label(self,textvariable=self.aircodeLabelVariable,anchor='w')
        aircodeLabel.grid(column=2,row=3,columnspan=3,sticky='EW',padx=5,pady=5)
        self.aircodeLabelVariable.set("Enter the 3 character airport code for each location")

        # Name cannot be blank reminder
        self.nameAlertVariable = tkinter.StringVar()
        nameAlert = tkinter.Label(self,textvariable=self.nameAlertVariable, anchor='w',fg='red')
        nameAlert.grid(column=2,row=2,sticky='EW',padx=5,pady=5)

        # Individual Travel label - Alert message to user
        self.individualAlertVariable = tkinter.StringVar()
        individualAlertMessage = tkinter.Label(self,textvariable=self.individualAlertVariable,anchor='w',fg='red')
        individualAlertMessage.grid(column=0,row=6,columnspan=5,sticky='EW',padx=5,pady=5)

        # Individual Travel label - confirmation message to user
        self.individualMessageVariable = tkinter.StringVar()
        individualMessage = tkinter.Label(self,textvariable=self.individualMessageVariable,anchor='w')
        individualMessage.grid(column=0,row=5,columnspan=4,sticky='EW',padx=5,pady=5)

        # Batch input filename ERROR label
        self.inputFileErrorLabelVariable = tkinter.StringVar()
        inputFileErrorLabel = tkinter.Label(self,textvariable=self.inputFileErrorLabelVariable,anchor='w')
        inputFileErrorLabel.grid(column=2,row=9,sticky='EW',padx=5,pady=5)

        # Batch output filename ERROR label
        self.outputFileErrorLabelVariable = tkinter.StringVar()
        outputFileErrorLabel = tkinter.Label(self,textvariable=self.outputFileErrorLabelVariable,anchor='w')
        outputFileErrorLabel.grid(column=2,row=10,sticky='EW',padx=5,pady=5)


# --- Text Entry Fields --- #

        # Name Entry field
        self.nameEntryVariable = tkinter.StringVar() # sets the variable for the data in the text field
        self.nameEntry = tkinter.Entry(self,textvariable=self.nameEntryVariable)
        self.nameEntry.grid(column=1,row=2,sticky='EW',padx=5,pady=5)

        # Home Entry field
        self.homeEntryVariable = tkinter.StringVar() # sets the variable for the data in the text field
        self.homeEntry = tkinter.Entry(self,textvariable=self.homeEntryVariable)
        self.homeEntry.grid(column=1,row=3,sticky='EW',padx=5,pady=5)

        # Travel Entry field 1
        self.travelEntryVariable1 = tkinter.StringVar() # sets the variable for the data in the text field
        self.travelEntry1 = tkinter.Entry(self,textvariable=self.travelEntryVariable1)
        self.travelEntry1.grid(column=1,row=4,sticky='EW',padx=5,pady=5)

        # Travel Entry field 2
        self.travelEntryVariable2 = tkinter.StringVar() # sets the variable for the data in the text field
        self.travelEntry2 = tkinter.Entry(self,textvariable=self.travelEntryVariable2)
        self.travelEntry2.grid(column=2,row=4,sticky='EW',padx=5,pady=5)

        # Travel Entry field 3
        self.travelEntryVariable3 = tkinter.StringVar() # sets the variable for the data in the text field
        self.travelEntry3 = tkinter.Entry(self,textvariable=self.travelEntryVariable3)
        self.travelEntry3.grid(column=3,row=4,sticky='EW',padx=5,pady=5)

        # Travel Entry field 4
        self.travelEntryVariable4 = tkinter.StringVar() # sets the variable for the data in the text field
        self.travelEntry4 = tkinter.Entry(self,textvariable=self.travelEntryVariable4)
        self.travelEntry4.grid(column=4,row=4,sticky='EW',padx=5,pady=5)

        # Batch input file field
        self.batchInputEntryVariable = tkinter.StringVar() # sets the variable for the data in the text field
        self.batchInputEntry = tkinter.Entry(self,textvariable=self.batchInputEntryVariable)
        self.batchInputEntry.grid(column=1,row=9,sticky='W',padx=5,pady=5)

        # Batch output file field
        self.batchOutputEntryVariable = tkinter.StringVar() # sets the variable for the data in the text field
        self.batchOutputEntry = tkinter.Entry(self,textvariable=self.batchOutputEntryVariable)
        self.batchOutputEntry.grid(column=1,row=10,sticky='W',padx=5,pady=5)


# --- Buttons ---#

        # Submit Button Individual # refers command to agent method: get individual best route
        nameButton = tkinter.Button(self,text="Submit Individual Details", command=self.onIndividualButtonClick)
        nameButton.grid(column=4,row=5,padx=5,pady=5)

        # Submit Button Batch # refers command to agent method: get batch best route (calls the read csv for employee with filename given, then gets best routes.
        homeButton = tkinter.Button(self,text="Submit for Batch Processing", command=self.onBatchButtonClick)
        homeButton.grid(column=4,row=11,padx=5,pady=5)


# --- General settings  ---#

        self.grid_columnconfigure(0,weight=1)   # allows columns to expand as window is resized horizontally.
        self.resizable(True,True)  # allows resizing horizontal and vertical
        self.minsize(750,380)
        self.update() # this line and the next keep the widget form consatntly resizing to fit
        self.geometry(self.geometry())
        self.nameEntry.focus_set() # sets cursor focus to the text field
        self.nameEntry.selection_range(0, tkinter.END) # selects all in the text field (default text clears when user types)


# --- Methods for GUI ---#

    def onIndividualButtonClick(self):
        ''' action for when individual button is clicked '''

        # display submitted details to the GUI
        self.individualMessageVariable.set(("Salesperson: %s     Home Airport: %s     Travel Airports: %s, %s, %s, %s " % (self.nameEntryVariable.get(), self.homeEntryVariable.get(),self.travelEntryVariable1.get(),self.travelEntryVariable2.get(),self.travelEntryVariable3.get(),self.travelEntryVariable4.get())))

        # get the info from entry fields
        employeeInfo = [self.nameEntryVariable.get(),self.homeEntryVariable.get(),self.travelEntryVariable1.get(),self.travelEntryVariable2.get(),self.travelEntryVariable3.get(),self.travelEntryVariable4.get()]
        notInLookup = []

        # transform airport entries to uppercase
        for each in employeeInfo[1:]:
            index = employeeInfo.index(each)
            each = each.upper()
            employeeInfo[index] = each
        # check that airport codes are in the airport lookup
        for aircode in employeeInfo[1:]:
            if aircode not in lookup.airport_info:
                notInLookup.append(aircode)

        if employeeInfo[0] == '': #
            self.nameAlertVariable.set('Name cannot be blank')
        elif len(notInLookup) > 0:             # Display error message
            self.individualAlertVariable.set( "The following airport codes were not found: %s. Please check your details and try again. " % notInLookup[:] )
        else:
            self.individualAlertVariable.set("") # clear the alert label
            # send info to the agent
            individualResult = agent.getIndividualResult(employeeInfo)
            # display results
            self.individualResultsVariable.set(( "Your best cost option is: %s, Total Cost: Euro %s " % (individualResult[:-1],individualResult[-1])))
            # clear the text from the entry fields and reset the values.
            self.nameEntryVariable.set("")
            self.homeEntryVariable.set("")
            self.travelEntryVariable1.set("")
            self.travelEntryVariable2.set("")
            self.travelEntryVariable3.set("")
            self.travelEntryVariable4.set("")

    def onBatchButtonClick(self):
        ''' action for when batch button is clicked '''
        # get the filenames from the GUI
        inputFilename = self.batchInputEntryVariable.get()
        outputFilename = self.batchOutputEntryVariable.get()

        try:
            fi = open(inputFilename, 'r')
            fi.close()
            print("good input file")
            self.inputFileErrorLabelVariable.set('') # clear the alert label
            try:
                fo = open(outputFilename, 'w')
                fo.close()
                print("good output file")
                self.outputFileErrorLabelVariable.set('') # clear the alert label

                # send filename to agent
                resultsFile = agent.getBatchResult(inputFilename,outputFilename)
                self.batchResultsLabelVariable.set(('Results are saved to the following filename: %s' % (str(resultsFile))))
            except IOError:
                self.outputFileErrorLabelVariable.set('The filename you entered for uploading is not writable. Please enter a different filename.')
        except IOError:
            self.inputFileErrorLabelVariable.set('The filename you entered for uploading is not readable. Please enter a different filename.')
            print("Error: can\'t find file or read data")

def runGUI():
    lookup = Lookup()
    lookup.readAirport()
    lookup.readCountryCurrency()
    lookup.readCurrencyRate()
##    agent = TravelAgent(lookup)
    app = simpleapp_tk(None)
    app.title('SuperSales Travel Planner') # title for GUI
    app.wm_iconbitmap('Airplane_silhouette.ico') # icon for GUI
    app.mainloop()

if __name__ == '__main__':
    lookup = Lookup()
    lookup.readAirport()
    lookup.readCountryCurrency()
    lookup.readCurrencyRate()
    agent = TravelAgent(lookup)
    app = simpleapp_tk(None)
    app.title('SuperSales Travel Planner') # title for GUI
    app.wm_iconbitmap('Airplane_silhouette.ico') # icon for GUI
    app.mainloop()

