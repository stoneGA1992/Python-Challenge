# First import the module
import os 

# Module for reading CSV files
import csv 

csvpath = os.path.join('..','Resources','election_data.csv')

# Intializing Variables
votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

 # Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

     # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header= next(csvreader)
    
    # Setting up variables outside of the loop
    votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    tooley_votes = 0

    # Adding up the votes
    for row in csvreader:
        votes = votes + 1

        if row[2] == "Khan":
            khan_votes = khan_votes + 1

        elif row[2] == "Correy":
            correy_votes= correy_votes + 1

        elif row[2] == "Li":
            li_votes = li_votes + 1

        else:
            tooley_votes = tooley_votes + 1

    # Calculate %s

    khan_percent = (khan_votes / votes)

    correy_percent = (correy_votes / votes)

    li_percent = (li_votes / votes)

    tooley_percent = (tooley_votes / votes)


    # Find the Winner

winner = max(khan_votes, li_votes, correy_votes, tooley_votes)

if winner == khan_votes:
    name = "Khan"

elif winner == li_votes:
    name = "Li"

elif winner == correy_votes:
    name = "Correy"

else:
    name = "O'Tooley "



print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
print(f"Khan: {khan_percent:.3%}, ({khan_votes})")
print(f"Correy: {correy_percent:.3%}, ({correy_votes})")
print(f"Li: {li_percent:.3%}, ({li_votes}) ")
print(f"O'Tooley: {tooley_percent:.3%}, ({tooley_votes})")
print("--------------------------")
print(f"Winner: {name}")
print("--------------------------")

 #Set up Output File
output_file = os.path.join('..','Resources','election_data_results.text')

with open(output_file,"w",) as newfile:

    newfile.write(f"Election Results\n")
    newfile.write(f"--------------------------\n")
    newfile.write(f"Total Votes: {votes}\n")
    newfile.write("--------------------------\n")
    newfile.write(f"Khan: {khan_percent:.3%}, ({khan_votes})\n")
    newfile.write(f"Correy: {correy_percent:.3%}, ({correy_votes})\n")
    newfile.write(f"Li: {li_percent:.3%}, ({li_votes}) \n")
    newfile.write(f"O'Tooley: {tooley_percent:.3%}, ({tooley_votes})\n")
    newfile.write("--------------------------\n")
    newfile.write(f"Winner: {name}\n")
    newfile.write("--------------------------\n")