import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

from branch.models import Results
import csv
with open("allotment.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
     z = Results()
     z.roll_no = row[0]
     z.name = row[1]
     z.curr_branch = row[2]
     z.dest_branch = row[3]

     z.save()
