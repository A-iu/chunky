import csv
import fileinput
import re


filename = "lexique_avec_POS_nettoye.csv"  # File name
dico = {} #on crée un dico pour avec les termes du lexique comme clé et les pos comme valeur

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')  # on lit le lexique au format csv

    fields = next(csvreader)  # Read header
    for row in csvreader:     # Read rows
        dico[row[0]]=row[1]


print(dico)
for line in fileinput.input(): #pour un texte en entrée
    line.rstrip()
    line=line.replace("’","’ ") #on rajoute un espace après l'apostrophep pour récupérer les DET et PREP concernés : l', d'
    line=line.replace("."," .") #même chose pour les apostrophes, mais avant le caractère
    line=line.replace(","," ,") #même traitement que les points pour les virgules
    line=line.replace("-t-"," -t- ") #puisqu'on y a droit espace aussi de part et d'autre du -t- euphonique
    res=re.split(r"\s+",line) #segmentation sur les espaces
    token_prec = "" #déclaration de la chaîne token précédent
    etat=0 #initiatlisation d'un compteur
    chunk="" #déclaration de la chaîne chunk
    coupe=0 #iniitialisation du compteur pour couper
    for token in res:
        token_min=token.strip("“") #pour les tokens en minuscules, couper sur le "“"
        if token_prec in ["","!","?",".",":",",","»"]: #de même, pour les signes de ponctuation
            coupe=1
            token_min=token_min.lower() #mettre les caractères initiaux en minuscules pour pouvoir lancer le lexique et les règle dessus.
        pos=dico.get(token_min,0) #parcourir le texte avec les règles du lexique
        if pos !=0: #instruction conditionnelle de l'algo
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
