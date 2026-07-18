import time
import cv2
print("Welcome to my math trainer!")
time.sleep(2)
print("2+2?")
n1= int(input())
if n1 == 4 :
    print("Good job!!")
else :
    print("YOU NEED TO TRAINING YOUR MATHS!!!!!")
time.sleep(2)
print("34+56?")
a = int(input())
if a == 90 :
    print("GOOD JOB!")
else :
    print("YOU NEED TO TRAINING YOUR MATHS!!!!!")
time.sleep(2)
print("If you want to continue to use my bot, follow me in github :)")
time.sleep(10)
print("That was a joke you can continue to use my bot but follow me ANYWAY ❤️")
time.sleep(5)
print("4x9?")
b = int(input())
if b == 36 :
    print("Did you follow me???")
    time.sleep(2)
    print("I see that you are a math genius!")
else : 
    print("😢😢😢")
time.sleep(4)
print("The next one is very hard!")
time.sleep(2)
print("45x3?")
print("😎")

c = int(input())
if c == 135 :
    print("The next one is very very hard")
else :
    print(":()")
time.sleep(2)
print("So...")
time.sleep(3)
print("63x7?")
d = int(input())
if d == 441 :
    print("WOW")
else :
    print("...:()")
time.sleep(2)
print("146x5?")
e = int(input())
if e == 730 :
    print("THE NEXT...")
else :
    print("FOLLOW ME NOW OR ...")
time.sleep(2)
print("378x6?")
time.sleep(7)
print("TIME IS UP!!!")
f = int(input())
if f == 2268 :
    print("...Ready for the next one?")
else :
    print("...")
time.sleep(2)
print("THE LAST ONE...")
time.sleep(5)
print("...😈")
time.sleep(5)
print("5738x46")
time.sleep(25)
print("TIME IS UP!!")
g = int(input())
if g == 263948 or "263948" or 263(",")+948 :
    print("OH MY GOD YOU'RE SO SMART!")
else :
    print("YOU = NOOB😈")
time.sleep(15)
print("AH YOU WAIT 15sec BECAUSE YOU WANT ANOTHER CHANCE?")
time.sleep(5)
print("CLOSE YOUR LAPTOP NOW")
time.sleep(2)
print("Close your laptop or in 10 seconds... ")
time.sleep(5)
print("...5seconds")
time.sleep(3)
print("2seconds...")
time.sleep(2)
print("I JUST TAKE THE CONTROL OF YOUR LAPTOP!!!!")
time.sleep(3)
print("😈😈😈😈😈😈😈😈😈😈😈😈😈😈😢😢🐸😜😎")
time.sleep(3)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Impossible d'ouvrir la caméra.")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Camera", frame)

    # Appuie sur q pour quitter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAAHAHAHAHA!!!!!!")
    print("I CAN DO ANYTHING ON YOUR LAPTOP!!!!!!!")
    time.sleep(2)
    print("...")
    print("FOLLOW ME ON GITHUB OR I AM GOING TO CONTINUE TO DO ANYTHING ON YOUR LAPTOP!!!")
    time.sleep(2)
    print("😈😈😈🙏")

camera.release()
cv2.destroyAllWindows()
