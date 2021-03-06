#!/usr/bin/python3
import ftplib
import os

# Ouverture de connexion
ftp = ftplib.FTP('ADRESSE DE VOTRE FTP')
ftp.login("votre login", "votre mdp")
ftp.cwd('/chemin de votre ftp qui contiennent vos données/')
os.chdir('/chemin de votre dossier qui recevra vos données')

#Lister des fichiers
filenames = ftp.nlst()

for filename in filenames:

    print("En cours de téléchargement... -> répertoire "NOM DE VOTRE FICHIER" LE BUREAU ;) " + filename)
    with open( filename, 'wb' ) as file :
        ftp.retrbinary('RETR %s' % filename, file.write)

        file.close()

ftp.quit()