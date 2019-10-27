import csv

TotalMonths = 0
NetProfitLoss = 0
BiggestIncrease = 0
BiggestIncreaseDate = ""
BiggestDecrease= 0
BiggestDecreaseDate =""

with open("budget_data.csv") as csv1:
    data = csv.DictReader(csv1, delimiter=',')
   
  
    for row in data:
        TotalMonths +=1
        NetProfitLoss += float(row["Profit/Losses"])
        if(float(row["Profit/Losses"])>0):
            #print(str(float(row["Profit/Losses"]))+ "is greater than 0.")
            if(float(row["Profit/Losses"])>BiggestIncrease):
                BiggestIncrease = float(row["Profit/Losses"])
                #print(row["Date"]+ " is biggest.")
                BiggestIncreaseDate = str(row["Date"])
        elif (float(row["Profit/Losses"])<0):
            if(float(row["Profit/Losses"])<BiggestDecrease):
                BiggestDecrease=  float(row["Profit/Losses"])
                BiggestDecreaseDate = str(row["Date"])

outputText1 = ""
outputText1+=("_________PyBank____________\n")
outputText1+=("Total Months: "+ str(TotalMonths)+"\n")
outputText1+=(f"Net Profit/Loss: ${NetProfitLoss}\n")
outputText1+=("Average Loss: $" + str(round(NetProfitLoss / TotalMonths,2))+"\n")
outputText1+=("Biggest Increase: "+ BiggestIncreaseDate + ": $" + str(BiggestIncrease)+"\n")
outputText1+=("Biggest Decrease: "+ BiggestDecreaseDate + ": -$" + str(BiggestDecrease *-1)+"\n")
print(outputText1)

#Write to txt file:
filename = "PyBankText.txt"
file1= open(filename,"w")
file1.write(outputText1)
file1.close()
print(f"File {filename} created and closed.")