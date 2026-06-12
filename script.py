import csv
import fileinput
import re


filename = "lexique_avec_POS_nettoye.csv"  # File name
fields = []  # Column names
rows = []    # Data rows
dico = {}

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')  # Reader object

    fields = next(csvreader)  # Read header
    for row in csvreader:     # Read rows
        dico[row[0]]=row[1]
        rows.append(row)

    print("Total no. of rows: %d" % csvreader.line_num)  # Row count

print('Field names are: ' + ', '.join(fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" ")
    print('\n')
print(dico)
for line in fileinput.input():
    line.rstrip()
    line=line.replace("’","’ ")
    res=re.split(r"(\s+)",line)
    #print(res)
    token_prec = ""
    for token in res:
        token_min=token
        if token_prec in ["","!","?","."]:
            token_min=token.lower()
        pos=dico.get(token_min,0)
        if pos !=0:
            print(token,pos)
        token_prec=token
    #print(line)

