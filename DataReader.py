'''
Parsia Hedayat, phedayat@ucsd.edu

This class defines a DataReader object. Its purpose is to create lists of the
dates (events) within an academic year and the number of people that signed-in
to them to create a plot of them.

One plot represents an entire academic year of data regarding sign-ins per
event.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataReader:
    filename = ''
    df = None

    # Constructor initalizes filename and our dataframe, df (the csv)
    def __init__(self, filename):
        self.filename = filename
        self.df = pd.read_csv(filename)

    # Splice the dataframe accordsing to a specific date
    def spliceDf(self, date):
        currSplice = self.df[self.df.Timestamp == date]
        return currSplice ## splice of the dataframe

    # Returns the size of the splice specific to the date
    def spliceDfCount(self, date):
        currSplice = self.df[self.df.Timestamp == date]
        return currSplice.Timestamp.size

    # Create a list of the number of attendees per date (event)
    def createCountList(self):
        cList = []
        i = 0
        while i < self.df.Timestamp.size:
            spliceSize = self.spliceDfCount(self.df.at[i, 'Timestamp'])
            cList.append(spliceSize)
            i += spliceSize
        return cList

    # Create a list of all dates in dataframe
    def createDatesList(self):
        dList = []
        i = 0
        while i < self.df.Timestamp.size:
            date = self.df.at[i, 'Timestamp']
            spliceSize = self.spliceDfCount(date)
            dList.append(date)
            i += spliceSize
        return dList

    def getAverage(self, data):
        sum = 0
        for i in data:
            sum += i
        return (sum / len(data))

    # Create and show a plot with data xAxis and yAxis
    def createPlot(self, xAxis, yAxis, fig):
        tickCount = np.arange(len(xAxis))
        plt.figure(figsize=(15, 15))
        #plt.subplot(2, 1, fig)
        plt.subplots_adjust(hspace=.5)
        plt.plot(xAxis, yAxis)
        plt.title('Sign-ins per Event')
        plt.xlabel('Dates')
        plt.ylabel('# of Attendees')
        plt.grid(True)
        plt.xticks(tickCount, xAxis, rotation='vertical')
        plt.margins(0.2)


    def funPrint(self):
        print(self.date)
        print(self.filename)

r = DataReader('sign-ins.csv')
r.createPlot(r.createDatesList(), r.createCountList(), 2)

s = DataReader('sign-ins2.csv')
s.createPlot(s.createDatesList(), s.createCountList(), 1)

print(r.getAverage(r.createCountList()))
print(s.getAverage(s.createCountList()))

plt.show()
