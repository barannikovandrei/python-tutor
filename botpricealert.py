#The programm is in french 

import requests
from bs4 import BeautifulSoup
import time
import re

url = "https://www.tezenis.com/be/fr/product/chemise_manches_longues_garcon_toile_coton_effet_lin-4ML1291.html?dwvar_4ML1291_Z_COL_TEZ=350Z" #YOU CAN CHANGE THE URL IF YOU WANT

ancien_prix = 10.50 #And change the price 

while True:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        page = requests.get(url, headers=headers).text
        soup = BeautifulSoup(page, "html.parser")

        # Cherche tous les textes contenant €
        texte = soup.get_text()

        prix_trouves = re.findall(r"\d+,\d+\s?€", texte)

        if prix_trouves:
            prix = prix_trouves[0]
            prix = float(prix.replace(",", ".").replace("€", ""))

            print("Prix actuel :", prix, "€")

            if prix < ancien_prix:
                print("🔔 ALERTE ! Le prix a baissé !")
                print("Ancien prix :", ancien_prix, "€")
                print("Nouveau prix :", prix, "€")

                break

        else:
            print("Prix introuvable")

    except Exception as e:
        print("Erreur :", e)

    time.sleep(60)
