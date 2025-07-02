##Pybank

##Set path

import os
import csv

pybankdata = os.path.join("..", "Resources", "budget_data.csv")
output = os.path.join("..", "pybank.txt")

##Set parameters

months = 0
profitloss = 0
changes = []
averagechange = 0.0

#read csv

with open(pybankdata) as csvfile:
    csvreader = csv.reader(delimeter = ",")

    header = next(csvreader)

## make calculations    
    first_row = next(csvreader)
    months = months +=1
    profitloss = profitloss+=int(row[1])
    prev_net = int(row[1])
        
    for row in csvreader:   
        months = months+=1
        profitloss = profitloss+=int(row[1])
        change = int(row[1])-prev_net
        changes.append(change)
        prev_net = int(row[1])
        
averagechange = sum(changes)/len(changes)
greatestincrease = max(changes)
greatestdecrease = min(changes)
        
##print answer

print("Financial Analysis\n___________________________\nTotal Months: " + str(months) + "\nNet Profit/Loss: " + str(profitloss) + "\nAverage Change: " + str(averagechange) + "\nGreatest Increase: " + str(greatestincrease) + "\nGreatest Decrease: " + str(greatestdecrease)

##output file