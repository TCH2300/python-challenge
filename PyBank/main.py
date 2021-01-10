# import modules
import os
import csv

# set file path
csv_path = os.path.join('Resources', 'budget_data.csv')



# lists
date_total = []
profit_loss = []
change = []


total_profit_loss = 0


# open csv and user reader to iterate through loop
with open(csv_path) as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        dates = row[0]
        date_total.append(dates) # update date_total list
        total_profit_loss += float(row[1]) # to caluculte total net
        total_profit_loss_formatted = '${:0,.0f}'.format(total_profit_loss)
        total_pl = row[1]
        profit_loss.append(total_pl)
        delta = row[2]
# -----------------------------------------
# total months
# -----------------------------------------
total_months = len(date_total)
#print(total_months)
# -----------------------------------------       
# to get change /b/ months  
# -----------------------------------------    
i = 1
while i < len(profit_loss):
    delta = (float(profit_loss[i]) - float(profit_loss[i-1]))
    i = i + 1
    change.append(delta)
#print(change)
#print(sum(change) / len(change)) 

# ----------------------------------------
# average change caluculation
# ----------------------------------------
total = sum(change)
count = len(change)
average = float(total / count)
average_formatted = '${:,.2f}'.format(average)
#print(average_formatted)

# ----------------------------------------
# greatest increase and date
# ----------------------------------------
max_change = max(change)
#print(max_change)
max_change_formatted = '${:0,.0f}'.format(max_change)
#print(max_change_formatted)
max_index = change.index(max_change) 
#print(max_index)
max_date = max_index + 1
#print(max_date)
max_date_change = str(date_total [max_date]) + (" ") + "(" + str(max_change_formatted) + ")"
#print(max_date_change)

# ----------------------------------------
# greatest decrease and date
# ----------------------------------------
min_change = min(change)
min_change_formatted = '${:0,.0f}'.format(min_change)
min_index = change.index(min_change) 
#print(min_index)
min_date = min_index + 1
#print(min_date)
min_date_change = str(date_total [min_date]) + (" ") + "(" + str(min_change_formatted) + ")"
#print(min_date_change)

# ----------------------------------------
# final print
# ----------------------------------------
total_months = len(date_total)
line1 = ("Financial Analysis")
line2 = ("Number of Months: " + str(total_months))
line3 = ("Total Net: " + str(total_profit_loss_formatted))
line4 = ("Average Change: " + "$" +" "+ str(average_formatted))
line5 = ("Greatest Increase in Profits: " + str(max_date_change))
line6 = ("Greatest Decrease in Profits: " + str(min_date_change))
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
# -------------------------------------------
# write to txt file
# -------------------------------------------
with open('analysis.txt', 'w') as txt_file:
    txt_file.writelines(line1)
    txt_file.write("\n")
    txt_file.writelines(line2)
    txt_file.write("\n")
    txt_file.writelines(line3)
    txt_file.write("\n")
    txt_file.writelines(line4)
    txt_file.write("\n")
    txt_file.writelines(line5)
    txt_file.write("\n")
    txt_file.writelines(line6)