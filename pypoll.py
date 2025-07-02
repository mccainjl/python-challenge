##Pypoll

##Import Data

import os
import csv

pypolldata = os.path.join("Resources", "election_data.csv")
pypolloutput = os.path.join("electionoutput.txt")

##Set up parameters

candidates = []
votes = {}
totalvotes = 0


##Open CSV File

with open(pypolldata) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
## Make tallies

    for row in csvreader:
        totalvotes+=1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate] = 0
        votes[candidate] = votes[candidate] + 1

winner = max(votes.values())

print("\nElection Results \n------------------------------\nTotal Votes: " + str(totalvotes) + "\n-------------------------------------\n")
for candidate in votes:
    print(candidate)
        



##Print output



##Write output file