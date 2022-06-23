# Data we need to retrieve
# 1. Total number of votes cast
# 2. Complete list of all candidates
# 3. Votes for each candidate
# 4. % of Votes each candidate won
# 5. Winner by popular vote

import csv

import os

dir(csv)

#Assign a variable for the file to load and the path
file_to_load = 'Resources\election_results.csv'

#Open the election results file
with open(file_to_load) as election_data: 
    
    # To do: read and analyze the data here

    #Read the file
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)
    










