# import modules
import os
import csv

# Specify filepath for data sources: budget_data_1.csv OR budget_data_2.csv
csvfilepath = os.path.join('raw_data','budget_data_2.csv')

# Open the file using csv.reader. Specify revenueData variable to hold content.
with open(csvfilepath, newline='') as revenueData:
    csvreader = csv.reader(revenueData, delimiter=',')

    # Create variables, lists, and dictionary to store corresponding data
    totalMonths = 0
    totalRevenue = 0
    monthlyChange = 0
    
    grtIncrease = 0
    grtDecrease = 0
    
    firstRevenue = 0
    lastRevenue = 0
    totalRevenue = 0

    revChange1 = []
    date1 = []
    table = {}

    grtIncreaseDate = 0
    grtDecreaseDate = 0

    firstRow = next(csvreader)  # Skip header row
    firstRevenueRow = next(csvreader) # Capture row with first revenue 
    firstRevenue = int(firstRevenueRow[1]) # Get first revenue from revenue column (index 1)
    # print(firstRevenue)

    # Iterate through all revenue data
    for row in csvreader:
        
        # Calculate and store totals in corresponding variables 
        totalMonths += + 1
        totalRevenue += int(row[1])
        lastRevenue = int(row[1])
        
        # Identify date index and store all dates in list
        date = str(row[0])
        date1.append(date)
        # print(date)

        # Calculate and store monthly and total monthly revenue changes in variables and list
        monthlyChange += lastRevenue - firstRevenue
        revChange = lastRevenue - firstRevenue
        # print(change)

        revChange1.append(revChange)
        # print(change1)
        
        # Reset firstRevenue to previous revenue
        firstRevenue = lastRevenue
    
    # Exit for loop and calculate average revenue change
    avgChange = monthlyChange / totalMonths
   
    # Add one to account for first row outside of loop
    totalMonths += + 1 
    totalRevenue = totalRevenue + int(firstRevenueRow[1])

    # Obtain greatest increase and decrease from corresponding lists
    grtDecrease = min(revChange1)
    grtIncrease = max(revChange1)

    # Join lists into dictionary capturing revenue changes and corresponding month
    table = dict(zip(date1, revChange1))
    # print(table)
    
    # Iterate through dictionary
    for date1, revChange1 in table.items():
        # print(table)
        
        # Capture date that corresponds with the greatest increase
        if (revChange1 == grtIncrease):
            grtIncreaseDate = date1

        # Capture date that corresponds with the greatest decrease
        elif (revChange1 == grtDecrease):
            grtDecreaseDate = date1

    # print(grtIncreaseDate)  
    # print(grtDecreaseDate)          

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total Revenue: $" + str(totalRevenue))
print("Average Revenue Change: $" + str(avgChange))
print("Greatest Increase in Revenue: " + str(grtIncreaseDate) + " ($" + str(grtIncrease) + ")")
print("Greatest Decrease in Revenue: " + str(grtDecreaseDate) + " ($" + str(grtDecrease) + ")")

# Specify path for storing the output file 
pyBankOutputPath = os.path.join('.', 'pyBankOutput2.txt') 

# Open the file using "write" mode. Specify csvfile variable to hold content.
with open(pyBankOutputPath, 'w', newline='') as textfile:
   
    textfile.writelines("Financial Analysis\n")
    textfile.writelines("----------------------------\n")
    textfile.writelines("Total Months: " + str(totalMonths) + "\n")
    textfile.writelines("Total Revenue: $" + str(totalRevenue) + "\n")
    textfile.writelines("Average Revenue Change: $" + str(avgChange) + "\n")
    textfile.writelines("Greatest Increase in Revenue: " + "($" + str(grtIncrease) + ")" + "\n")
    textfile.writelines("Greatest Decrease in Revenue: " + "($" + str(grtDecrease) + ")" + "\n")