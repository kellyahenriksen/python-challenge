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
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
   
    count = 0
    sum = 0
    profits_losses = []
    first_row = (next(csvreader))
    prev_num = int(first_row[1])
    for row in csvreader:
        count= count + 1
        sum = sum + int(row[1])
        profits_losses.append(prev_num - int(row[1]))
        prev_num = int(row[1])
print(profits_losses)

    
 
sum_num = 0
for x in range(len(profits_losses)-1):
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
print(avg)

# The greatest increase in profits (date and amount) over the entire period
print(max(profits_losses))

# The greatest decrease in losses (date and amount) over the entire period
print(min(profits_losses))