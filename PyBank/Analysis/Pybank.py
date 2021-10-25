# Import

import os
import csv

# FIGURE OUT THE FILEPATH ON YOUR COMPUTER
csvpath = "03-Python/Instructions/PyBank/Resources/budget_data.csv"

# read in the CSV data into memory - a list of lists
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    # print(f"CSV Reader: {csv_header}")

     # store all my rows as list of lists
    all_rows = []
    for row in csvreader:
        temp_row = row
        temp_row[1] = int(temp_row[1])
        all_rows.append(temp_row)

# Find total months (equal to the amount of rows in data set)
months_total = len(all_rows)

# Find the value for the sum of the total profits
profits_all = [x[1] for x in all_rows]
profits_sum = sum(profits_all)

# Start counting from the second row so it doesn't include the header
changes = []
for i in range(len(all_rows) - 1): 
    curr_profit = all_rows[i][1]
    next_profit = all_rows[i + 1][1]

    change = next_profit - curr_profit
    changes.append(change)

# Get average changes

avg_change = round(sum(changes)/len(changes), 2)

max_change = max(changes)
min_change = min(changes)

# Get change indexes

max_change_index = changes.index(max_change) + 1
max_month = all_rows[max_change_index][0]

min_change_index = changes.index(min_change) + 1
min_month = all_rows[min_change_index][0]

# Conver CSV to TXT File

out_path = "pybank.txt"
with open(out_path, "w") as f:
    f.write(f"Financial Analysis\n\n")
    f.write(f"----------------------------\n")
    f.write(f"Total Months: {months_total}\n")
    f.write(f"Total: ${profits_sum}\n")
    f.write(f"Average Change: ${avg_change}\n")
    f.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    f.write(f"Greatest Decrease in Profits: {min_month} (${min_change})\n")

