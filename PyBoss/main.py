# Import modules 
import os
import csv

# Specify filepath for data sources: employee_data1.csv OR employee_data2.csv
csvfilepath = os.path.join('raw_data', "employee_data1.csv")

# Open the file using dict reader. Specify employeeData variable to hold content.
with open(csvfilepath, newline='') as employeeData:
    csvreader = csv.DictReader(employeeData, delimiter=',')

    # Create lists to capture corresponding data
    IDs = []
    DOBs = []
    SSNs = []
    States = []
    FirstNames = []
    LastNames = []
    
    # Create ditionary of US State names and corresponding abbreviations
    StateAbbrev = {'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'}    

    # Interate through all rows in EmployeeData; Note csv.DictReader skips headers.
    # Add relevant data into corresponding list using append function and format data appropriately.
    for row in csvreader: 
        IDs.append(row['Emp ID'])
        FirstNames.append(row['Name'].split(' ')[0])
        LastNames.append(row['Name'].split(' ')[1])
        DOBs.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        SSNs.append('***-**-' + row['SSN'].split('-')[2])
        States.append(StateAbbrev[row['State']])

    # Zip all lists into tuple named nEmployeeData
    nEmployeeData = zip(IDs, FirstNames, LastNames, DOBs, SSNs, States)

 # Specify path for storing the output file 
pyBossOutputPath = os.path.join('.', 'pyBossOutput.csv') 

# Open the file using "write" mode. Specify csvfile variable to hold content.
with open(pyBossOutputPath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers): Emp ID,First Name,Last Name,DOB,SSN,State
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write all rows for nEmployeeData
    csvwriter.writerows(nEmployeeData)
   