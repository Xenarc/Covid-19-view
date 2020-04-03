import matplotlib.pyplot as plt 
import pandas as pd
from scipy import optimize
import numpy as np
import csv

Dates = []
ACT = []
NSW = []
NT = []
QLD = []
SA = []
TAS = []
VIC = []
WA = []

datafile = open('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
for row in datareader:
  data.append(row) 

Dates = data[0][0].split(',')
ACT = data[9][0].split(',')
NSW = data[10][0].split(',')
NT = data[11][0].split(',')
QLD = data[12][0].split(',')
SA = data[13][0].split(',')
TAS = data[14][0].split(',')
VIC = data[15][0].split(',')
WA = data[16][0].split(',')

Dates = Dates[4:]
ACT = [float(i) for i in ACT[4:]]
NSW = [float(i) for i in NSW[4:]]
NT = [float(i) for i in NT[4:]]
QLD = [float(i) for i in QLD[4:]]
SA = [float(i) for i in SA[4:]]
TAS = [float(i) for i in TAS[4:]]
VIC = [float(i) for i in VIC[4:]]
WA = [float(i) for i in WA[4:]]

fig, graph = plt.subplots(3, 2)


old = 0
deltas = []
for x in VIC:
  deltas.append(x-old);
  old = x

totals = np.array([sum(x) for x in zip(ACT, NSW, NT, QLD, SA, TAS, VIC, WA)])
totals = [1 if x == 0 else x for x in totals]
xVals = np.array(range(len(Dates)))
graph[0][0].plot(xVals, totals)
graph[0][0].set_title('Total cases')

graph[0][1].plot(xVals, totals)
p = np.polyfit(xVals, np.log(totals), 1)
graph[0][1].plot(xVals, np.exp(p[1])*np.exp(p[0]*xVals))
p = np.polyfit(xVals[35:], np.log(totals[35:]), 1)
graph[0][1].plot(xVals[35:], np.exp(p[1])*np.exp(p[0]*xVals[35:]))
graph[0][1].set_yscale('log')
graph[0][1].set_title('Total cases (log)')

graph[1][0].plot(xVals, ACT)
graph[1][0].plot(xVals, NSW)
graph[1][0].plot(xVals, NT)
graph[1][0].plot(xVals, QLD)
graph[1][0].plot(xVals, SA)
graph[1][0].plot(xVals, TAS)
graph[1][0].plot(xVals, VIC)
graph[1][0].plot(xVals, WA)
graph[1][0].legend(["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"], loc='upper left')
graph[1][0].set_title('Cases per state')


graph[2][0].plot(xVals, deltas)
deltas = pd.Series(deltas).rolling(window=10).mean()
graph[2][0].plot(xVals, deltas)
graph[2][0].legend(["Delta", "Moving Average (n=10)"], loc='upper left')
graph[2][0].set_title('Deltas')

graph[1][1].plot(xVals, ACT)
graph[1][1].plot(xVals, NSW)
graph[1][1].plot(xVals, NT)
graph[1][1].plot(xVals, QLD)
graph[1][1].plot(xVals, SA)
graph[1][1].plot(xVals, TAS)
graph[1][1].plot(xVals, VIC)
graph[1][1].plot(xVals, WA)
graph[1][1].legend(["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"], loc='upper left')
graph[1][1].set_yscale('log')
graph[1][1].set_title('State Cases (log)')

plt.subplots_adjust(left = 0.05, right = 1, bottom = 0.05, top = 0.95, wspace = 0, hspace=0.2)

# function to show the plot 
plt.show()
