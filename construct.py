import os
import time
import sys

def main():
	#dir='/home/git/projet-1.git/'
	dir=os.path.dirname(sys.argv[0])
	
	j=0
	for dossier, sous_dossiers, fichiers in os.walk(dir):
		sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.']
		for fichier in fichiers:
			j+=1

	tab=[[" "]*4 for x in range(j)]
	i=0

	for dossier, sous_dossiers, fichiers in os.walk(dir):
		for fichier in fichiers:
			sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.']
			tab[i][0]=fichier
			tab[i][1]=os.path.abspath(fichier)
			tab[i][2]=time.ctime(os.path.getctime(fichier))
			tab[i][3]=""
		#    (fichier +" "+(os.path.abspath(fichier)+" "+str((os.path.getctime(dir)))+" "))
			i+=1
		   

	return tab; 