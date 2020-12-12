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
print("Election Results")
print("-----------------------------")

# The total number of votes cast
print(f'Total Votes: {count}')
for candidate in candidates:
    print(f'{candidate}: {percentages[candidate]}% ({votes[candidate]})')

# The winner of the election based on popular vote.
print(f'Winner: {winner}')

textpath = os.path.join('Analysis', 'output.txt')
with open(textpath,'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Votes: {count}\n")
    textfile.write(f"Khan: {percentages["Khan"]}% ({votes["Khan"]})\n")
    textfile.write(f"Correy: {percentages["Correy"]}% ({votes["Correy"]})\n")
    textfile.write(f"Li: {percentages["Li"]}% ({votes["Li"]})\n")
    textfile.write(f"O'Tooley: {percentages["O'Tooley"]}% ({votes["O'Tooley"]})\n")
    textfile.write(f"Winner: {winner}")