# ---------------
# Import Modules
# ---------------
import os
import csv
# -----------------
# Set CSV file path
# -----------------
csv_path = os.path.join('Resources', 'election_data.csv')

# ------------------------
# Lists and Dictionaries
# -----------------------
candidates = []
votes_dict = {}

# ---------------------------------------
# Open csv file and use reader to iterate
# ---------------------------------------
with open(csv_path) as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)
    #print(header)
# ----------------------------------------------
# Put candidates into a list and get total votes
# ----------------------------------------------
    for row in reader:
        names = row[2]
        candidates.append(names)
    total_votes = (len(candidates))
    #print(total_votes)
# ------------------------------------------------------------------
# Put candidates list into a dictionary to see votes per candidate
# ------------------------------------------------------------------
    for i in set(candidates):
        votes_dict[i] = candidates.count(i)
#print(votes_dict)

line1= ("Election Results")
print(line1)
print('---------------------------------')
line2= ("Total Votes:" + str(total_votes))
print(line2)
print('----------------------------------')
# --------------------------------
# Percent per candidate
# --------------------------------
sum = sum(votes_dict.values())

for k, v in votes_dict.items():
    percent = (round(v * 100 / sum))
    #print(k)
    #print(v)
    #print(k, percent, v)
    print(k,":", percent,"%", "(",v,")")
print("----------------------------------")
    
# ------------------------------
# Find Winner
# ------------------------------
winner = max(votes_dict, key = votes_dict.get)
#print(winner)
line4= ("Winner: " + str(winner))
print(line4)
print("-----------------------------------")

# ------------------------------
# write to txt file
# ------------------------------
with open('analysis.txt', 'w') as txt_file:
    txt_file.writelines(line1)
    txt_file.write("\n")
    txt_file.write("--------------------------")
    txt_file.write("\n")
    txt_file.writelines(line2)
    txt_file.write("\n")
    txt_file.write("--------------------------")
    txt_file.write("\n")
    txt_file.write("Could not figure out how to get line 55 of code to print to txt file :(" )
    txt_file.write("\n")
    txt_file.write("--------------------------")
    txt_file.write("\n")
    txt_file.writelines(line4)
    
# was unable to figure out how to get indivdual lines of each dictionary key and value to print to text.
    


