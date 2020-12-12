# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    next(csvreader)

    count = 1
    sum = 0
    profits_losses = []
    greatest_increase = ""
    greatest_number = 0
    greatest_decrease = ""
    lowest_number = 0
    first_row = (next(csvreader))
    sum = int(first_row[1])
    prev_num = int(first_row[1])
    for row in csvreader:
        count= count + 1
        sum = sum + int(row[1])
        profits_losses.append(int(row[1])-prev_num)
        if (int(row[1])- prev_num)>greatest_number:
            greatest_number = (int(row[1])-prev_num)
            greatest_increase = row[0]
        if (int(row[1])- prev_num)<lowest_number:
            lowest_number = (int(row[1])-prev_num)
            greatest_decrease = row[0]
        prev_num = int(row[1])
    
sum_num = 0
for x in range(len(profits_losses)):
    sum_num = sum_num + profits_losses[x]           

avg = sum_num / len(profits_losses)
 
 # Your task is to create a Python script that analyzes the records to calculate each of the following:
print("Financial Analysis")
print("-----------------------------")

# The total number of months included in the dataset
print(f"Total Months:{count}")

# The net total amount of "Profit/Losses" over the entire period
print(f"Total: ${sum}")

# # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print(f'Average Change:  {round(avg,2)}')

# The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {greatest_increase} {max(profits_losses)}')

# The greatest decrease in losses (date and amount) over the entire period
print(f'Greatest Decrease in Profits: {greatest_decrease} {min(profits_losses)}')

textpath = os.path.join('Analysis', 'output.txt')
with open(textpath,'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Months:{count}\n")
    textfile.write(f"Total: ${sum}\n")
    textfile.write(f'Average Change:  {round(avg,2)}\n')
    textfile.write(f'Greatest Increase in Profits: {greatest_increase} {max(profits_losses)}\n')
    textfile.write(f'Greatest Decrease in Profits: {greatest_decrease} {min(profits_losses)}\n')