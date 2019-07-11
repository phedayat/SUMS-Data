from DataReader import DataReader

x = DataReader('sign-ins.csv')

x.createPlot(x.createDatesList(), x.createCountList())

y = DataReader('sign-ins2.csv')

y.createPlot(y.createDatesList(), y.createCountList())
