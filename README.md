### Python Bootcamp Challenge

Hello! This is my answer to the Python Homework Challenge at the GA Tech Data Analytics and Visualization Bootcamp. This assignment covered the first topic, Python, and is done in oldschool python script to run in a console. The assignment comprised of two parts:

## Pybank

I had to create a python script to analyze a set of financial records (budget_data.csv in the Resources folder) to provide the following calcuations:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" for each month from the previous month over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

I did this by reading in the data with the csv module and defining a function that would loop through each row of the dataset while counting up the number of months and adding up the profit/loss for each row. A challenge I had to overcome was having the profits/losses subtracted from the previous row to measure change. I did this by storing the current row value as a variable and referring back to it in each successive loop. Finally, I presented all results by presenting them to the console and outputting them in a text file. 

## PyPoll

In this challenge, I had to analyze a set of poll data called election_data.csv (in the Resources folder). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. I had to calculate each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

Again, I did this by looping through the data with csvreader. In order to analyze the tallied votes for each candidate, I used a dictionary with the candidate's name as the key and their total votes as the value. Each loop would determine if a candidates name was already in the dictionary, and if it was not, would append the name and add the vote; if it was, it would add to the existing vote tally for that candidate. Again I provided output in the console and via a text file in the folder. 
