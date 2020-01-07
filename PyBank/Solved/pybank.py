# First import the module
import os 

# Module for reading CSV files
import csv 

csvpath = os.path.join('..','Resources','budget_data.csv')

# Intializing Variables
months = 0
profit_loss= 0
average = 0
monthly_change = []
month_counter = []
change = 0
largest_increase = 0
largest_decrease = 0
largest_increase_month = 0
largest_decrease_month = 0

#  Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

     # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header= next(csvreader)
    row = next(csvreader)

    #Setting up variables outside the loop
    last_row = int(row[1])
    months = months + 1
    profit_loss += int(row[1])
    largest_increase = int(row[1])
    largest_increase_month = row[0]
    largest_decrease = int(row[1])
    largest_decrease_month = row[0]

    # Reading data
    for row in csvreader:
        months = months + 1
        profit_loss += int(row[1])
        
        change = int(row[1]) - last_row
        last_row = int(row[1])
        monthly_change.append(change)
        month_counter.append(row[0])

        # Largest Increase
        if int(row[1]) > largest_increase:
            largest_increase = int(row[1])
            largest_increase_month = row[0]

        # Largest Decrease
        if int(row[1]) < largest_decrease:
            largest_decrease = int(row[1])
            largest_decrease_month = row[0]
       


    average = sum(monthly_change)/len(monthly_change)

    highest_profit = max(monthly_change)
    lowest_loss = min(monthly_change)


   
# Print Analysis

print("Financial analysis")
print("--------------------------")
print(f"Total Months: {months}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits:, {largest_increase_month}, (${highest_profit})")
print(f"Greatest Decrease in Profits:, {largest_decrease_month}, (${lowest_loss})")

# Set up Output File
output_file = os.path('..','Resources','budget_analysis.text')

with open(output_file,"w",) as newfile:

    newfile.write(f"Financial Analysis\n")
    newfile.write(f"--------------------------\n")
    newfile.write(f"Total Months: {months}\n")
    newfile.write(f"Total: ${profit_loss}\n")
    newfile.write(f"Average Change: ${average}\n")
    newfile.write(f"Greatest Increase in Profits:, {largest_increase_month}, (${highest_profit})\n")
    newfile.write(f"Greatest Decrease in Profits:, {largest_decrease_month}, (${lowest_loss})\n")
