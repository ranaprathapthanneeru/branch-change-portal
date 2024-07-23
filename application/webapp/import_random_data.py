import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

from branch.models import Student
import csv
with open("initialise_data.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
     z = Student()
     row[0]=int(row[0])
     z.roll_no = row[0]
     row[1]=float(row[1])
     z.cpi = row[1]
     z.password = row[2]
     z.category = row[3]
     z.curr_branch = row[4]
     z.save()
