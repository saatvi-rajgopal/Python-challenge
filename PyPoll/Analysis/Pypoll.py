# Import

import os
import csv

# FIGURE OUT THE FILEPATH ON YOUR COMPUTER
csvpath = "02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

# read in the CSV data into memory - a list of lists
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    # print(f"CSV Reader: {csv_header}")

     # store all my rows as list of lists
    all_rows = []
    for row in csvreader:
        all_rows.append(row)

total_votes =  len(all_rows)

# Create a dictionary for storing votes per each candidate

votes = {}

for row in all_rows:
    candidate = row[2]

    if candidate in votes.keys():
        # add 1 to their votes
        votes[candidate] += 1
    else:
        votes[candidate] = 1

print(votes)

# get winner of votes
max_votes = ""
init_votes = 0 
for winner in votes:
    votes_won = votes[winner]
    if votes_won > init_votes:
        init_votes = votes_won
        max_votes = winner

# write to TXT file

out_path = "pypoll.txt"
with open(out_path, "w") as f:
    f.write(f"Election Results\n")
    f.write(f"-----------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write(f"-----------------------------\n")

    for winner in votes.keys():
        f.write(f"{winner}: {round(votes[winner]/total_votes * 100)}% ({votes[winner]})\n")

    f.write(f"-----------------------------\n")
    f.write(f"Winner: {max_votes}\n")
    f.write(f"-----------------------------\n")