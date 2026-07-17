#This bot calculate the result(+,-,x or /) of the first and the second number that you write.

import time
print("What is your name?")
a = str(input())
print("Hello "+a+".")
time.sleep(2)
print("Give me 2 numbers")
n1 = int(input())
n2 = int(input())
print("Choose : +, -, x or /")
r = str(input())
if r == "+" :
    print(n1+n2)
elif r == "-" :
    print(n1-n2)
elif r == "x" or "X" :
    print(n1*n2)
else :
    print(n1/n2)

time.sleep(2)
print("Chatbot create by Andreï Barannikov")
