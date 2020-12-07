import csv
csvpath= 'PyBank/Resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv'
  
with open(csvpath) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    csv_header=next(csv_file)
    print(f"Header:{csv_header}")
    # Total number of months included in the data set  
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
    
    for row in csv_reader:
        monthcount +=1
        total += int(row[1])

        date.append(row[0])
        profit = int(row[1])
        profits.append(profit)
    
        cd=0
        if previous_profit != 0: 
            cd = profit - previous_profit
            difference.append(cd)
        previous_profit = profit
        
        
        if cd > increase['profits']:
            increase['profits'] = cd
            increase['month'] = row[0]
        if cd < decrease['losses']:
            decrease['losses'] = cd
            decrease['month'] = row[0]
            
    average_change = sum(difference) / len(difference)
    

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {monthcount}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase['month']} ${increase['profits']}")
print(f"Greatest Decrease in Profits: {decrease['month']} ${decrease['losses']}")





