import csv
import fileinput
import re


filename = "lexique_avec_POS_nettoye.csv"  # File name
dico = {}

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')  # Reader object

    fields = next(csvreader)  # Read header
    for row in csvreader:     # Read rows
        dico[row[0]]=row[1]


print(dico)
for line in fileinput.input():
    line.rstrip()
    line=line.replace("’","’ ")
    line=line.replace("."," .")
    line=line.replace(","," ,")
    line=line.replace("-t-"," -t- ")
    res=re.split(r"\s+",line)
    token_prec = ""
    etat=0
    chunk=""
    coupe=0
    for token in res:
        token_min=token.strip("“")
        if token_prec in ["","!","?",".",":",",","»"]:
            coupe=1
            token_min=token_min.lower()
        pos=dico.get(token_min,0)
        if pos !=0:
            #print(token,pos)
            if etat==0:
                coupe=1
            etat=1
        else:
            etat=0
        if (coupe==0):
            chunk+=" "+token
        else:
            print(chunk,"\n")
            chunk=token
        coupe=0
        token_prec=token_min
    print(chunk,"\n")
