#coding: utf-8

import json
import csv
import requests

fichier = "banq.csv"

a = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

entete = {
	"User-Agent": "Laurent Corbeil",
	"From": "514-827-3723"
}

l1 = range(1000,2001)
for numero in l1:
	
	url = a + str(numero)
	#print(url)
	req = requests.get(url,headers=entete)
	#print(req)

	if req.status_code == 200:
		infos = req.json()
		#print(infos)
		i = infos ["titre"]
		#m4a = i.find("url"[1])
		#print(mp4)
		if infos["type"] == "audio":
			s = []
			s.append(infos["titre"][:(i.find("/"))])
			s.append(infos["createurs"][0])
			s.append(infos["dateCreation"])
			s.append(infos["descriptionMat"])
			#s.append(infos["url"])
			print(infos["titre"][:(i.find("/"))])
			print(infos["createurs"][0])
			print(infos["dateCreation"])
			print(infos["descriptionMat"])
			#print(infos["url"])
			#Incapable de saisir le texte contenant la bonne adresse URL pour le téléchargement
			#J'ai donc modifié l'URL par défaut avec les éléments nécessaires

			url0 = (infos["iris"]).replace("0000","/1/")
			#print(url0)
			url1 = (infos["url"].replace("ark:","bitstream"))
			#print(url1)
			url2 = ".m4a"
			url3 = url1 + url0 + url2
			#print(url3)
			s.append(url3)
			print(url3)
			print("~"*80)
		

			f2 = open(fichier, "a")
			banq = csv.writer(f2)
			banq.writerow(s)

		
			

	

