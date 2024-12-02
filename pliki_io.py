import os
import shutil
import numpy as np

f = open("dane.txt","r",encoding="utf-8")

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()

print(f.closed)
print("_"*50)
f = open("dane.txt","r",encoding="utf-8")
print(f.read())

f.close()

g = open("message.txt","w",encoding="utf-8")
g.write("linia  nowe dane\n")
g.close()
h = open("message.txt","a",encoding="utf-8")
h.write("nowa linia  kolejne dane\n")

h.close()

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty!")
else:
    print("plik nie istnieje!")

print("_"*50)

ściezka = "./mojepliki"
if os.path.exists(ściezka):
    shutil.rmtree(ściezka)
    print("usunięto katalog z danymi")
else:
    print("katalog nie istnieje!")
