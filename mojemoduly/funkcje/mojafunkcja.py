def czytaj_liste(lista):
    print(f"______ lista: {lista} _____")
    for i,j in enumerate(lista):
        print(f"element listy nr {i+1} -> wartość: {j}")
        
def czytaj_slownik(slownik):
    print(f"_____ słownik {slownik} _____")
    for x,y in slownik.iter():
        print(f"klucz: {x} -> wartość: {y}")
