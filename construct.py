#!/usr/bin/python

import os
import time
import sys
import subprocess


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
	 
	# for dossier, sous_dossiers, fichiers in os.walk(dir):
		# sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.']
		# for fichier in fichiers:
			# print(os.path.abspath(fichier))
			# tab[i][0]=fichier
			# tab[i][1]=os.path.abspath(fichier)
			# tab[i][2]=time.ctime(os.path.getctime(fichier))
			# tab[i][3]=""
		# #    (fichier +" "+(os.path.abspath(fichier)+" "+str((os.path.getctime(dir)))+" "))
			# i+=1

	# traverse dossier directory, and list directories as dirs and files as files
	for dossier, sous_dossiers, fichiers in os.walk(dir):
		sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.']
		path = dossier.split(os.sep)
		for file in fichiers:
			if os.path.isfile(file):
				tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + file
				tab[i][1]=os.path.abspath(file)
				tab[i][2]=time.ctime(os.path.getctime(file))
				cmd="git log "+ file+ " | grep Author | cut -d' ' -f2 | head -1"
				tab[i][3]=subprocess.check_output(cmd, shell=True)
				print(subprocess.check_output(cmd, shell=True))
			elif os.path.isfile(dossier+"/"+file):
				tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + os.path.basename(dossier+"/"+file)
				tab[i][1]=os.path.abspath(dossier+"/"+file)
				tab[i][2]=time.ctime(os.path.getctime(dossier+"/"+file))
				cmd="git log "+ file+ " | grep Author | cut -d' ' -f2 | head -1"
				tab[i][3]=subprocess.check_output(cmd, shell=True)
			i+=1
			
	

	return tab; 