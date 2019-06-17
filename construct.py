#!/usr/bin/python
# coding: utf-8

import os
import time
import sys
import subprocess


def main():
	#recupere emplacement dossier
	dir=os.path.dirname(sys.argv[0])
	
	j=0
	dir_index = 0
	show_hide=False #affichage des dossiers cachés
	#bouclie d'initialisation du tableau qui sera retourné
	
	for dossier, sous_dossiers, fichiers in os.walk(dir): 
		if not show_hide:
			sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.']
		for fichier in fichiers:
			j+=1
		for sd in sous_dossiers:
			j+=1
	
	#tableau en 2d 
	#tab[indice][info]
	#info : 0- name ; 1- path ; 2- derniere mod ; 3- pusher
	tab=[[" "]*4 for x in range(j)]
	
	i=0

	#boucle qui parcours l'arborescence :
	for dossier, sous_dossiers, fichiers in os.walk(dir): 
		if not show_hide:
			sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.'] #supprime les dossiers cachés
		path = dossier.split(os.sep)
		
		change_directory=False #do once changement dossier
		if change_directory:
			dir_index = 0
			change_directory=False
			
		#pour chaque fichier dans l'arborescence
		for file in fichiers:
		
			if os.path.isfile(dossier+"/"+file): #si le fichier existe bien à l'endroit verifié
				name= (len(path) - len(dir.split(os.sep))) * '&nbsp&nbsp&nbsp&nbsp'
				if (len(path) - len(dir.split(os.sep))) > 0 :
					name += '├─' 
				name += os.path.basename(dossier+"/"+file)
				tab[i][0] = name
				#tab[i][1]=os.path.abspath(dossier+"/"+file) #emplacement dossier
				tab[i][2]=time.ctime(os.path.getctime(dossier+"/"+file))
				cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
				tab[i][3]=subprocess.check_output(cmd, shell=True)
			i+=1
		
		#si il existe des sous dossiers dnas le dossier actuel
		if(len(sous_dossiers)>0):
			change_directory = True
			name= (len(path) - len(dir.split(os.sep))) * '&nbsp&nbsp&nbsp&nbsp'
			if (len(path) - len(dir.split(os.sep))) > 0 :
				name += '└─' 
			name += os.path.basename(sous_dossiers[dir_index])
			tab[i][0] = name
			# tab[i][1]=os.path.abspath(dossier) #emplacement dossier
			tab[i][2]=time.ctime(os.path.getctime(dossier))
			cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
			tab[i][3]=subprocess.check_output(cmd, shell=True)
			i+=1
			
	#retorune le tableau comprenant l'ensemble des infos
	return tab; 
	
	
	
	
