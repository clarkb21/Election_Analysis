# Data we need to retrieve
# 1. Total number of votes cast
# 2. Complete list of all candidates
# 3. Votes for each candidate
# 4. % of Votes each candidate won
# 5. Winner by popular vote

import csv

import os

# Show what that directory does in Python: dir(csv)

#Assign a variable for the file to load and the path
file_to_load = 'Resources\election_results.csv'

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

total_votes = 0

 #Get all the candidate names 
candidate_options = []

# Create a dictionary to hold candidates and their total votes 
candidate_votes = {}

#candidate_votes = {"candidate_name1" : votes, "candidate_name2" : votes, "candidate_name3" : votes}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results file
with open(file_to_load) as election_data: 
    
    # To do: read and analyze the data here

    #Read the file
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader: 
    

    #Count up all votes, initialize total votes to zero (which needs to be done before the open statement)
        total_votes = total_votes + 1

        #print(total_votes)

    #Print the candidate name from each row
        candidate_name = row [2]

    #Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
        
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes: 
    votes = candidate_votes[candidate_name]

    vote_percentage = (float(votes) / float(total_votes)) *100

    #Determine wnning vote count and candidate

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes: ,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage

        winning_candidate = candidate_name

#Print the candidate name and percentage of votes
    # print(f"{candidate_name} : received {vote_percentage:.1f}% of the vote")

   #Print out the winning candidate, their vote count, and percentage 
        
winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    
print(winning_candidate_summary)

    












