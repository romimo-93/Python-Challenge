import csv
csvpath= 'PyBank/Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv'
#Open CSV as Reader 
with open(csvpath) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    csv_header=next(csv_file)
    print(f"Header:{csv_header}")

#Declare Variables
    monthcount=0
    total=0
    average_change=0
    date=[]
    profits=[]
    previous_profit=0
    difference=[]
    total_difference=0
    increase={"month": "", "profits": 0}
    decrease={"month": "", "losses": 0}
    
#The total number of months included in the dataset
    for row in csv_reader:
        monthcount +=1
        total += int(row[1])

#The net total amount of "Profit/Losses" over the entire period
        date.append(row[0])
        profit = int(row[1])
        profits.append(profit)
    
#Calculate the changes in "Profit/Losses" over the entire period, 
        cd=0
        if previous_profit != 0: 
            cd = profit - previous_profit
            difference.append(cd)
        previous_profit = profit
        
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period        
        if cd > increase['profits']:
            increase['profits'] = cd
            increase['month'] = row[0]
        if cd < decrease['losses']:
            decrease['losses'] = cd
            decrease['month'] = row[0]
#then find the average of those changes        
    average_change = sum(difference) / len(difference)
    
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {monthcount}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase['month']} ${increase['profits']}")
print(f"Greatest Decrease in Profits: {decrease['month']} ${decrease['losses']}")

output = open("PyBank/Analysis/file.txt","w")
analysis = output(file.txt, delimiter=',')
output.write(f"Financial Analysis")
output.write(f"----------------------------")
output.write(f"Total Months: {monthcount}")
output.write(f"Total: ${total}")
output.write(f"Average Change: ${average_change:.2f}")
output.write(f"Greatest Increase in Profits: {increase['month']} ${increase['profits']}")
output.write(f"Greatest Decrease in Profits: {decrease['month']} ${decrease['losses']}")









