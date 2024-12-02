# krotka
liczby = (1, 5, 2, 7, 47, 3, 85, 33, 83, 24)
wersje = [1.1, 1.2, 3.2, 3.4, 6.7, 6.8]

print(liczby)
print(wersje)

wersje.append(8.5)
print(wersje)


def policz(a, b, n, c):
    return (a + b) * (n - c), a + n, n ** 2


wynik = policz(4, 2, 5, 2)
print(wynik)
print(type(wynik))

drzewa = {"dąb", "sosna", "topola", "świerk", "jabłoń", "dąb"}
print(drzewa)
print(type(drzewa))

nb = [2, 5, 2, 1, 1, 3, 5, 7, 3, 2, 2, 3, 1, 1]
nb = list(set(nb))
print(nb)

s1 = "druzyna: 'Barcelona'"
print(s1)

s2 = "drużyna: \"Real Madryt\""
print(s2)

s3 = "GKS Katowice"
print(f"drużyna: \"{s3}\"")

drzewa.add("jodła")
print(drzewa)

drzewa.remove("topola")
print(drzewa)

drzewa.update(("topola", "jodła", "cyprys"))
print(drzewa)

# słownik
samochod = {
    "id": 11,
    "marka": "Jeep",
    "model": "Grand Jerokee",
    "kolor": "czarny",
    "rocznik": 2019,
    "kontrola": ["Kraków", "Lublin", "Lublin", "Bytom"]
}

print(samochod)

samochod["model"] = "Grand Cherokee Limited"
print(samochod)
samochod["poj"] = 3.8
print(samochod)
print(samochod.keys())
print(samochod.values())
print(samochod.items())
