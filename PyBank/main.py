# Import modules
import os
import csv
#Trackers and lists
total_months = 0
months = []
total_Profit_Loss = 0
last_Profit_Loss = 0
highest_Profit_Inc = 0
lowest_Loss_Dec = 999999999999
profit_Loss_Change = []
# path
budget_data = os.path.join(".", "budget_data.csv")
# Reading csv file
with open(budget_data, "r", newline="",) as csvfile:
# csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    print(budget_data)
    # Read header row
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    # Read each row of data after header
    for row in csvreader:
        print(row)   
        # Count the number of months
        total_months = total_months + 1
        # Net total Profit/Loss over period
        total_Profit_Loss = total_Profit_Loss + (int(row[1]))
        # Monthly change in Profit/Loss
        monthly_Profit_Loss_Change = int(row[1]) - last_Profit_Loss
        last_Profit_Loss = int(row[1])
        # Add monthly Profit/Loss changes in new column
        profit_Loss_Change.append(monthly_Profit_Loss_Change)
        # Find the average Profit/Loss Change
        avg_Profit_Loss_Change = round(sum(profit_Loss_Change)/total_months)
        # Greatest increase in Profits
        if (monthly_Profit_Loss_Change > highest_Profit_Inc):
            highest_Profit_Inc_Month = row[0]
            highest_Profit_Inc = monthly_Profit_Loss_Change
        # Greatest decrease in Losses
        if (monthly_Profit_Loss_Change < lowest_Loss_Dec):
            lowest_Loss_Dec_Month = row[0]
            lowest_Loss_Dec = monthly_Profit_Loss_Change

# Financial Anaylsis using f-strings for formatting
Results =(
f"Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {total_months} \n"
f"Total Profit/Loss: ${total_Profit_Loss} \n"
f"Average Profit/Loss Change: ${avg_Profit_Loss_Change} \n"
f"Greatest Increase in Profits: {highest_Profit_Inc_Month} (${highest_Profit_Inc}) \n"
f"Greast Decrease in Profits: {lowest_Loss_Dec_Month} (${lowest_Loss_Dec}) \n")
print(Results)

# Create a text file to export results
outputtxt = os.path.join(".", "budget_data_analysis.txt")
with open(outputtxt, "w") as txtfile:
    txtwriter = txtfile.write(Results)
    