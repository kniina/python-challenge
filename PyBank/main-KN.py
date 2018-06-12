import os
import csv

csvfilepath = os.path.join('/Users/kniina/GWDC201805DATA3-Class-Repository-DATA/Homework/03-Python/Instructions/PyBank/raw_data/budget_data_1.csv')

with open(csvfilepath, newline='') as revenueData:
    csvreader = csv.reader(revenueData, delimiter=',')
    # next(csvreader, None)

    totalMonths = 0
    totalRevenue = 0
    monthlyChange = 0
    
    grtIncrease = 0
    grtDecrease = 0
    
    firstRow = 0
    firstRevenue = 0
    lastRevenue = 0
    totalRevenue = 0

    change1 = []
    date1 = []
    table = {}

    firstRow = next(csvreader)  # Skips header row
    firstRevenue = next(csvreader) #Skips first 
    firstRevenue = int(firstRevenue[1])
    
    
    for row in csvreader:
        
        #calculating total number of months by counting rows in dataset
        totalMonths += + 1
        totalRevenue += int(row[1])
        lastRevenue = int(row[1])
        
        date = str(row[0])
        date1.append(date)
        # print(date)

        monthlyChange = monthlyChange + lastRevenue - firstRevenue
        change = lastRevenue - firstRevenue
        change1.append(change)
        # print(change1)
        
        firstRevenue = lastRevenue
    
    avgChange = monthlyChange / totalMonths
    totalMonths = totalMonths + 1
    grtDecrease = min(change1)
    grtIncrease = max(change1)

    table = dict(zip(date1, change1))
    print(table)
    

    # for date1, change1 in table.items():
    #     print(table)
        
        
    #     if (change1 > grtIncrease):
    #         grtIncrease = change1
    #         grtIncreaseDate = date1
    #         # print(grtIncreaseDate)
     

    #     elif (change1 < grtDecrease):
    #         grtDecrease = change1
    #         grtDecreaseDate = date1
            
# print(grtDecrease)
# print(grtIncrease)    

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total Revenue: $" + str(totalRevenue))
print("Average Revenue Change: $" + str(avgChange))
print("Greatest Increase in Revenue: " + "($" + str(grtIncrease) + ")")
print("Greatest Decrease in Revenue: " + "($" + str(grtDecrease) + ")")


# Specify path for storing the output file 
pyBankOutputPath = os.path.join('/Users/kniina/apps/python-challenge/PyBank/pyBankOutput.txt') 

# Open the file using "write" mode. Specify csvfile variable to hold content.
with open(pyBankOutputPath, 'w', newline='') as textfile:
    # csvwriter = csv.writer(textfile, delimiter='')
    textfile.writelines("Financial Analysis\n")
    textfile.writelines("----------------------------\n")
    textfile.writelines("Total Months: " + str(totalMonths) + "\n")
    textfile.writelines("Total Revenue: $" + str(totalRevenue) + "\n")
    textfile.writelines("Average Revenue Change: $" + str(avgChange) + "\n")
    textfile.writelines("Greatest Increase in Revenue: " + "($" + str(grtIncrease) + ")" + "\n")
    textfile.writelines("Greatest Decrease in Revenue: " + "($" + str(grtDecrease) + ")" + "\n")