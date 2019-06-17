#!/usr/bin/python
# coding: utf-8

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
		for sd in sous_dossiers:
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
		
		sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.'] #supprime les dossiers cachés
		change_directory=True
		path = dossier.split(os.sep)
		for sous_dossier in sous_dossiers:
			for file in fichiers:
				if os.path.isfile(file):
					tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + file
					tab[i][1]=os.path.abspath(file)
					tab[i][2]=time.ctime(os.path.getctime(file))
					cmd="git log "+ file+ " | grep Author | cut -d' ' -f2 | head -1"
					tab[i][3]=subprocess.check_output(cmd, shell=True)
					
				elif os.path.isfile(dossier+"/"+file):
					print(dossier+"/"+file)
					print(dossier+"/"+sous_dossier+"/"+file)
				### A REVOIR POUR LES SOUS DOSSIER ###
					if change_directory:
						change_directory=False
						tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + os.path.basename(dossier)
						tab[i][1]=os.path.abspath(dossier)
						tab[i][2]=time.ctime(os.path.getctime(dossier))
						cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
						tab[i][3]=subprocess.check_output(cmd, shell=True)
						i+=1
						tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + os.path.basename(dossier+"/"+file)
						tab[i][1]=os.path.abspath(dossier+"/"+file)
						tab[i][2]=time.ctime(os.path.getctime(dossier+"/"+file))
						cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
						tab[i][3]=subprocess.check_output(cmd, shell=True)
						
					else:
						tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + os.path.basename(dossier+"/"+file)
						tab[i][1]=os.path.abspath(dossier+"/"+file)
						tab[i][2]=time.ctime(os.path.getctime(dossier+"/"+file))
						cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
						tab[i][3]=subprocess.check_output(cmd, shell=True)
				elif os.path.isfile(dossier+"/"+sous_dossier+"/"+file):
					print(yep)
				i+=1
			
	

	return tab; 
	
	
	
	
	
		# for dossier, sous_dossiers, fichiers in os.walk(dir):
		
		# sous_dossiers[:] = [d for d in sous_dossiers if not d[0] == '.'] #supprime les dossiers cachés
		
		# path = dossier.split(os.sep)
		# for sous_dossier in sous_dossiers :
			# change_directory=True
			# for file in fichiers:
				# if os.path.isfile(file):
					# tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + file
					# tab[i][1]=os.path.abspath(file)
					# tab[i][2]=time.ctime(os.path.getctime(file))
					# cmd="git log "+ file+ " | grep Author | cut -d' ' -f2 | head -1"
					# tab[i][3]=subprocess.check_output(cmd, shell=True)
					
					
				# elif os.path.isfile(dossier+"/"+file):
					# print(dossier+"/"+file)
				# ### A REVOIR POUR LES SOUS DOSSIER ###
					# if change_directory:
						# change_directory=False
						# tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + os.path.basename(dossier)
						# tab[i][1]=os.path.abspath(dossier)
						# tab[i][2]=time.ctime(os.path.getctime(dossier))
						# cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
						# tab[i][3]=subprocess.check_output(cmd, shell=True)
						# i+=1
						# tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + os.path.basename(dossier+"/"+file)
						# tab[i][1]=os.path.abspath(dossier+"/"+file)
						# tab[i][2]=time.ctime(os.path.getctime(dossier+"/"+file))
						# cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
						# tab[i][3]=subprocess.check_output(cmd, shell=True)
						
					# else:
						# tab[i][0] = (len(path) - len(dir.split(os.sep))) * '---' + os.path.basename(dossier+"/"+file)
						# tab[i][1]=os.path.abspath(dossier+"/"+file)
						# tab[i][2]=time.ctime(os.path.getctime(dossier+"/"+file))
						# cmd="git log "+ dossier+"/"+file+ " | grep Author | cut -d' ' -f2 | head -1"
						# tab[i][3]=subprocess.check_output(cmd, shell=True)
				# elif os.path.isfile(dossier+"/"+sous_dossier+"/"+file):
					# print(yep)
				# i+=1