#Practicing IF else statements
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC")

else: 
    print("Open the windows")


# F string practice 
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
perecentage_votes = (my_votes / total_votes) *100

print("I received " + str(perecentage_votes) + "% of the total votes")

#Using F string
print(f"I received {my_votes / total_votes *100}% of the total votes.")

print(f"I received {perecentage_votes}% of the total votes.")

