#Iterate through a dictionary

counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438}

for county in counties_dict.keys():
    print(county)


for voters in counties_dict.values():
    print(voters)


for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Skill Drill 3.2.11

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
{

#More Skill Drills
voting_data = [''{"county": "Arapahoe", "registered_voters" : 422829} , {"county" : "Denver" , "registered_voters" : 463353}, {"county" : "Jefferson", "registered_voters" : 432438}]

for county, voters in voting_data.items():
    print(f"[county] county has [registered_voters: ,] registered voters.")
    

 





