##Pybank

##Set path

import os
import csv

pybankdata = os.path.join("Resources", "budget_data.csv")
pybankoutput = os.path.join("pybank.txt")

##Set parameters

months = 0
profitloss = 0
changes = []
averagechange = 0.0
maxincrease = 0
maxdecrease = 0
maxmonth = ""
minmonth = ""

#read csv

with open(pybankdata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

## make calculations    
    first_row = next(csvreader)
    months+=1
    profitloss+=int(first_row[1])
    prev_net = int(first_row[1])
        
    for row in csvreader:   
        months+=1
        profitloss+=int(row[1])
        change = int(row[1])-prev_net
        changes.append(change)
        prev_net = int(row[1])
        if change > maxincrease:
            maxincrease = change
            maxmonth = row[0]
        if change < maxdecrease:
            maxdecrease = change
            minmonth = row[0]
        
averagechange = sum(changes)/len(changes)
        
##print answer

print("\nFinancial Analysis\n--------------------------------\nTotal Months: " + str(months) + "\nNet Profit/Loss: $" + str(profitloss) + "\nAverage Change: $" + str(round(averagechange,2)) + "\nGreatest Increase: $" + str(maxincrease) + " " + maxmonth + "\nGreatest Decrease: $" + str(maxdecrease) + " " + minmonth)

##output file

with open(pybankoutput, "w") as txtfile:
    txtfile.write("\nFinancial Analysis\n--------------------------------\nTotal Months: " + str(months) + "\nNet Profit/Loss: $" + str(profitloss) + "\nAverage Change: $" + str(round(averagechange,2)) + "\nGreatest Increase: $" + str(maxincrease) + " " + maxmonth + "\nGreatest Decrease: $" + str(maxdecrease) + " " + minmonth)


    