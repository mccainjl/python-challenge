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

    header = next(csvreader)
    
## Make tallies

    for row in csvreader:
        totalvotes+=1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate] = 0
        votes[candidate] = votes[candidate] + 1

winner = max(votes.values())

##Print output

Election_results = "\nElection Results \n------------------------------\nTotal Votes: " + str(totalvotes) + "\n-------------------------------------\n"

candidate_votes = votes.get(candidate)
vote_percentage = float(candidate_votes) / float(totalvotes) * 100

voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

winner_announcement = f"-----------------------------------\nWinner: {winner}\n------------------------------------------"

print(Election_results)
print(voter_output)
print(winner_announcement)


##Write output file

with open(pypolloutput) as txtfile:
    txtfile.write(Election_results)
    txtfile.write(voter_output)
    txtfile.write(winner_announcement)