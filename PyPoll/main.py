# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.


# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. 
import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

   #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    count = 0
    candidates = []
    votes = {}
    percentages = {}
    winner = ""
    win_votes = 0
    for row in csvreader:
        count = count + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            votes[row[2]]=0
        else:
            votes[row[2]] = votes[row[2]]+1
for x in candidates:
    vote_percentage = round((votes[x]/count)*100,2)
    percentages[x] = vote_percentage
for x in votes:
    if win_votes < votes[x]:
        winner = x
        win_votes = votes[x]



# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# print(Election Results)
# print(-----------------------------)

# The total number of votes cast
print(count)

# A complete list of candidates who received votes
print(candidates)

# The percentage of votes each candidate won
print(percentages)

# The total number of votes each candidate won
print(votes)

# The winner of the election based on popular vote.
print(winner)