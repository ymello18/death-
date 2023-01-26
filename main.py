import matplotlib.pyplot as ply
import csv
import string
import matplotlib.patches as mpa
from matplotlib import pyplot


age = 1980
year = []
for k in range(0, 41):
  ages = str(age)
  year.append(ages)
  age = age + 1
# print(year)

file = open("death1.csv", "r")
dataIn = file.read()
file.close()
print(dataIn)
print("coucou")

valueBE = []
valueBE = dataIn.split("\n")
valueBE = valueBE.pop(0)
valueBE = valueBE.split(",")
valueBE = [int(item) for item in valueBE]

valueBF = []
valueBF = dataIn.split("\n")
valueBF = valueBF.pop(1)
valueBF = valueBF.split(",")
valueBF = [int(item) for item in valueBF]

valueRE = []
valueRE = dataIn.split("\n")
valueRE = valueRE.pop(2)
valueRE = valueRE.split(",")
valueRE = [int(item) for item in valueRE]
print(valueRE)

valueRF = []
valueRF = dataIn.split("\n")
valueRF = valueRF.pop(3)
valueRF = valueRF.split(",")
valueRF = [int(item) for item in valueRF]
print(valueRF)

axix = []
age = 1980
for k in range(0,9) :
  axix.append(age)
  for y in range(0,5) :
    axix.append('')
    age += 1
    
  

#Create a line graph with names on x-axis and numbers on  y-axis

ply.bar(year, valueBF, color='#B4E4F3')
ply.bar(year, valueBE, color="#008FBB")
ply.bar(year, valueRF, color='#CF0909')
ply.bar(year, valueRE, color='#FF6A6A')


ply.xlabel("Years")
# ply.xticks(rotation = 'vertical')
pyplot.gca().xaxis.set_ticklabels(axix, rotation = 60)

ply.ylabel("Number of Deaths")

legend = ply.legend(['Democrats State', 'Democrats Federal', 'Republicans State', 'Republicans Federal'], title="Policy party")

ply.show()