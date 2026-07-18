#IT'S A VIRUS IN FRENCH!!
import random
import time
import os
import pyautogui
import cv2
from datetime import datetime

# Liste de phrases
phrases = [
    "Bonjour je viens de prendre tout le controle de ton ordi!",
    "Python contrôle le monde.",
    "ALLER PLUS VITE",
    "JE VIENS DE PRENDRE LE CONTROLE DE TON ORDINATEUR!"
    "ABONNE TOI à MON GITHUB SI TU VEUX SURVIVRE "
]

# Sons (mets tes propres fichiers .wav ici)
sons = [
    "son1.wav",
    "son2.wav"
]


def parler():
    phrase = random.choice(phrases)
    os.system(f'say "{phrase}"')


def ouvrir_application():
    apps = [
        "Calculator",
        "Safari",
        "Notes",
        "Chess"
    ]

    app = random.choice(apps)
    os.system(f'open -a "{app}"')


def bouger_souris():
    x = random.randint(100, 1000)
    y = random.randint(100, 700)

    pyautogui.moveTo(x, y, duration=1)


def ecrire_message():
    messages = [
        "Hello Python !",
        "Je teste l'automatisation.",
        "Ceci est un robot."
    ]

    pyautogui.write(random.choice(messages), interval=0.05)


def prendre_capture():
    image = pyautogui.screenshot()

    nom = f"capture_{datetime.now().strftime('%H-%M-%S')}.png"

    image.save(nom)
    print("Capture sauvegardée :", nom)


def camera():
    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()

    if ret:
        cv2.imwrite("photo_camera.jpg", frame)
        print("Photo prise !")

    cam.release()


def jouer_son():
    son = random.choice(sons)

    if os.path.exists(son):
        os.system(f"afplay {son}")
    else:
        print("Son introuvable :", son)


def afficher_heure():
    print("Heure :", datetime.now())


# Actions possibles
actions = [
    parler,
    ouvrir_application,
    bouger_souris,
    ecrire_message,
    prendre_capture,
    camera,
    jouer_son,
    afficher_heure
]


print("🤖 Chaos Mode activé !")
print("CTRL+C pour arrêter")

while True:

    action = random.choice(actions)

    print("Action :", action.__name__)

    action()

    # Attendre entre deux actions
    temps = random.randint(5, 15)
    time.sleep(temps)
