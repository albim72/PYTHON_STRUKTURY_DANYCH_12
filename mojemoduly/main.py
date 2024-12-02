# import dane
# import dane as dn
# from dane import *
from dane import nrfilii as nf
from dane import book as bk

from funkcje.mojefunkcje import czytaj_liste
from funkcje.mojefunkcje import czytaj_slownik

print("__________ dane ___________")
print(nf)
print(bk)

print("__________ dane - za pomocą funkcji ___________")

czytaj_liste(nf)
czytaj_slownik(bk)
