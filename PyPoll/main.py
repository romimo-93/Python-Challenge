import csv
csvpath= 'PyPoll/Resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv'
#Open CSV as Reader
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

#Declare Variables
    votescast=0
    totalvotescast=0
    candidates=[]
    numberwon = {}
    percentwon=0
    winnername=""
    winnervotes=0
  
#The total number of votes cast
    for row in csv_reader:
        votescast +=1
    
#A complete list of candidates who received votes
#The total number of votes each candidate won
        if row[2] not in candidates:
            candidates.append(row[2])
            numberwon[row[2]]=0
        numberwon[row[2]]+=1
        
#Print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votescast}")
print(f"-------------------------")

#The percentage of votes each candidate won
for name in numberwon:
    votes = numberwon[name]
    percentage = votes / votescast
    pretty = percentage * 100
    print(f"{name}: {pretty:.3f}% ({votes})")

#The winner of the election based on popular vote.
    if votes > winnervotes: 
        winnervotes = votes
        winnername = name
#Print 
print(f"-------------------------")
print(f"Winner:{winnername}")
print(f"-------------------------")
