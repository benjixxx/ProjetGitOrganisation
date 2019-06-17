#!/bin/bash

#permet de connaitre le nombre de seconde depuis 01/01/1970 de la derniere modif 

t1=`find /backup/ -printf "%Td-%Tm-%Ty \n" | tail -1`
t2=`find /home/git/projet-1.git/ -printf "%Td-%Tm-%Ty \n" | tail -1`

#convertir le string provenant du format jj-mm-yy en int
echo $t1
echo $t2
# temps1=$(date -d $t1 +%s)
# temps2=$(date -d $t2 +%s)

#nommer le fichier et déclarer la source et la destination de l'archive
TIME=`date +%b-%d-%y`                      
FILENAME=backup-$TIME.tar.gz    
SRCDIR=/home/git/projet-1.git                  
DESDIR=/backup  

#Savoir si il y'a une une modif depuis le dernier archivage
if  [[ $t1 -ge $t2 ]]
then 
    #Savoir si le fichier existe dejà : vu qu'il y'a une modif de temps,on rm et on refait
    if ! [[ -e $DESDIR/$FILENAME ]]
    then
        tar -czf $DESDIR/$FILENAME $SRCDIR
    else
        rm -rf $DESDIR/$FILENAME
        tar -czf $DESDIR/$FILENAME $SRCDIR
    fi
else
    exit
fi
