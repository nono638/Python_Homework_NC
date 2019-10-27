import csv

TotalVotes = 0
CandidatesList=[]
CandidateDict={}
with open("election_data.csv") as csv2:
    thing = csv.DictReader(csv2, delimiter=',')
   
    for row in thing:
        TotalVotes+=1
        #print(str(row))
        if (row["Candidate"]) not in CandidatesList:
            CandidatesList.append(row["Candidate"])
            CandidateDict[row["Candidate"]] = 1
        else:
            CandidateDict[row["Candidate"]]+=1
    

    print(CandidateDict)
    # #make dictionary:
    
    # for v in CandidatesList:
    #     CandidateDict[v]=0

    # for RowAgain in thing:
    #     CandidateDict[RowAgain["Candidate"]] +=1
    
    

OutputText = ""


OutputText += "Total votes: " + str(TotalVotes)
ListOfCandidatesString = "List Of Candidates: "
for c in CandidatesList:
    ListOfCandidatesString+= c + ", "
OutputText += ("\n"+ListOfCandidatesString)
winner = ""
greatest=0
for k, v in CandidateDict.items():
    percentage = round((v / TotalVotes) *100,2)
    OutputText +=(f"\nCandidate {k} had {v} votes and {percentage}% of the vote.")
    if v > greatest:
        greatest = v
        winner = k
OutputText+= ("\nOverall Winner: "+ winner)

print(OutputText)
File_object = open("OutputText.txt","w")
File_object.write(OutputText)
if(File_object.closed == False):
    File_object.close()
    #print("file closed.")