# Git Autopush & Arborescence

Git Auto est un ensemble d'utilitaire mis à disposition pour gérer de manière automatique vos commits sur un Git.

## Dependence

Nécessite les packets suivants :

```bash
inotify-tools
proftp
python3
```

Nécéssite un serveur http / ftp configuré correctement avec une redirection exterieur (ip wan)

## Installation

Copier l'ensemble du dossier serveur sur votre serveur \
Copier le fichier 'autopush' dans votre dossier de repo. \
Configurer un serveur ftp sur le serveur du repo (en cas de git hors github) 

## Debug sans serveur
Possibilité d'executer le HttpServer.py afin de verifier le bon fonctionnement de l'ensemble \
Attention, HttpServer.py n'est PAS un serveur de production \
Visiter localhost:8080/index.py


## Usage

Client:
```bash 
cd /chemin/du/repo/locale
sudo chmod +x autopush.py
python3 autopush.py
```

Lancement auto au boot:
```bash
sudo nano /etc/rc.local
<chemin/du/autopush.py> &
```

Ouvrir le fichier index.py sur votre serveur depuis votre navigateur


## Authors
Clément, Benjamin, Vincent
