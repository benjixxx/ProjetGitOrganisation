#!/bin/bash


#Installation des packages necessaires si non present
if [[ `dpkg -l | grep inotify` == "" ]] 
then
	echo "*** INSTALLATION DES DEPENDANCES EN COURS..***"
	sudo apt-get install incron
	sudo apt install inotify-tools
fi

#Configuration utilisateur 
if [[ `ls -a | grep .auth` == "" ]]
then #si aucun user n'a été trouvé
	echo "*** CONFIGURATION GIT ***"	
	read -p "Login :" login
	read -s -p "Password :" password
	read -p "URL du git :" url
	echo $login $password $url > .auth
	git config credential.helper store
	sshpass -p "$password" git clone "$login@$url"
	cd `ls -d */`
else #sinon, recuperation login
	login=`cat .auth | cut -f1 -d" "`
	password=`cat .auth | cut -f2 -d" "`
	url=`cat .auth | cut -f3 -d" "`
	git config credential.helper store
	cd `ls -d */`
	sshpass -p $password git pull "$login@$url"
fi

#git config credential.helper store #stockage mdp via git



branch="master"
#for file in $(find . -not -path '*/\.*')
for file in $(ls)
do
	echo $file
	#inotifywait -q -m -e CLOSE_WRITE --format="git commit -m 'auto commit' %w && git push origin $branch" $file
	inotifywait -q -m -e CLOSE_WRITE --format="git add * && git commit -m 'autocommit on change' %w && git push" $file | sh &
done
