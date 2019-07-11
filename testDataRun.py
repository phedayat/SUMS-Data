import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("sign-ins.csv")

# Splice the dataframe accordsing to a specific date
def spliceDf(date):
    currSplice = df[df.Timestamp == date]
    return currSplice ## splice of the dataframe

BGN = spliceDf('10/9/2018')

print(BGN)

for d in df.iterrows():
    print(d[0] * 4)
    print(df.at[d[0], 'Timestamp'])

eventsList = []
for r in df.iterrows():
    eventsList.append(df.at[r[0], 'Timestamp'])

print(eventsList[0])

# Returns the size of the splice specific to the date
def spliceDfCount(date):
    currSplice = df[df.Timestamp == date]
    return currSplice.Timestamp.size

print(spliceDfCount('10/9/2018'))

# Create a list of the number of attendees per date (event)
def createCountList():
        cList = []
        i = 0
        while i < 405:
            spliceSize = spliceDfCount(df.at[i, 'Timestamp'])
            cList.append(spliceSize)
            i += spliceSize
        return cList

countList = createCountList()
print(countList)

# Create a list of all dates in dataframe
def createDatesList():
    dList = []
    i = 0
    while i < 405:
        date = df.at[i, 'Timestamp']
        spliceSize = spliceDfCount(date)
        dList.append(date)
        i += spliceSize
    return dList

datesList = createDatesList()
print(datesList)

# Create and show a plot with data xAxis and yAxis
def createPlot(xAxis, yAxis):
    tickCount = np.arange(len(xAxis))

    plt.plot(xAxis, yAxis)
    plt.title('Sign-ins per Event')
    plt.xlabel('Dates')
    plt.ylabel('# of Attendees')
    plt.grid(True)
    plt.xticks(tickCount, xAxis, rotation='vertical')
    plt.margins(0.2)
    plt.show()

createPlot(datesList, countList)
