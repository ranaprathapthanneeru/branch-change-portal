from branch.models import BranchChange
import csv
with open("input_options.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
     z = BranchChange()
     z.roll_no = row[0]
     z.name = row[1]
     row[2]=float(row[2])
     z.cpi = row[2]
     z.category = row[3]
     z.preference1 = row[4]
     z.preference2 = row[5]
     z.preference3 = row[6]
     z.preference4 = row[7]
     z.preference5 = row[8]
     z.preference6 = row[9]
     z.preference7 = row[10]
     z.preference8 = row[11]
     z.preference9 = row[12]
     z.preference10 = row[13]
     z.preference11 = row[14]
     z.preference12 = row[15]
     z.preference13 = row[16]
     z.preference14 = row[17]
     z.preference15 = row[18]
     z.preference16 = row[19]
    
     z.save()
