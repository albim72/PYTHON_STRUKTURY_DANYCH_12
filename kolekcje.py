print("kolekcje Pythona")
print("ala ma kota")

a = 101
print(a)
print(type(a))

#komentarz podstawowy
"""
komentarz wieloliniowy
dokumentacyjny
"""

info = """
kilka słów
i więcej
455235325325
"""

print(info)

a = "jedynka"
print(a)
print(type(a))

#lista
imiona = ["Maria","Anna","Jan","Maria","Jan","Olaf"]
print(imiona)
print(type(imiona))
print(imiona[3])
print(imiona[1:4])
print(imiona[:5])
print(imiona[2:])
print(imiona[-1])
print(imiona[-2:])
miasto = "Katowice"

print(miasto)
print(miasto[0])
print(len(miasto))

print(miasto[::-1])

b = "105.6"
print(b)
print(type(b))

b = (float)(b)
print(b)
print(type(b))

c = "44"

print(8*c)

print(eval(c)*8)

code = """
a = 5345435
b =5786

print(a-b)
"""

print(code)

exec(code)
