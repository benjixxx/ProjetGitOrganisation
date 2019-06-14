import os
import time
dir='/home/git/projet-1.git/'
j=0

for dossier, sous_dossiers, fichiers in os.walk(dir):
    for fichier in fichiers:
        j+=1

tab=[[" "]*4 for x in range(j)]
i=0

for dossier, sous_dossiers, fichiers in os.walk(dir):
    for fichier in fichiers:
        print (i)
        tab[i][0]=(fichier)
        tab[i][1]=(os.path.abspath(fichier))
        tab[i][2]=(str((os.path.getctime(dir))))
        tab[i][3]=""
    #    (fichier +" "+(os.path.abspath(fichier)+" "+str((os.path.getctime(dir)))+" "))
        i+=1
       

print (tab)