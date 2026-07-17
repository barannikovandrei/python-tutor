# PLAY THE FAMOUS FRENCH GAME UN DEUX TROIS PIERRE FEUILLE CISEAU!!!
import time
import random
print("T'es pret à jouer à un-deux-trois pierre feuille ciseau?")
a = str(input())
print("alors c'est parti!!!")
print("1")
time.sleep(1)
print("2")
time.sleep(1)
print(3)
time.sleep(1)
print("pierre, feuille, ciseau")
choix = random.choice(["Pierre", "Feuille", "Ciseaux"])

print("L'ordinateur a choisi : "+choix)
