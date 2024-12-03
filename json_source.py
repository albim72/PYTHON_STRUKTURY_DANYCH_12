import json

json_dane = """
{
"name":"Jan Kot",
"age":30,
"city":"Gdańsk",
"is_student":"False",
"last_ids":[23,67,865],
"address":{
        "street":"Złota",
        "local_nb":"6/45"
    }
}
"""

print(json_dane)
print(type(json_dane))

try:
    print("parsowanie danych")
    datadict = json.loads(json_dane)
    print(datadict)
    print(type(datadict))

    print("_"*50)
    print("DANE ->")
    print(f"imię i nazwisko: {datadict['name']}\n"
          f"wiek: {datadict['age']}\n"
          f"miasto: {datadict['city']}\n"
          f"czy jest studentem? {datadict['is_student']}\n"
          f"id zamówień: {datadict['last_ids']}\n"
          f"ulica: {datadict['address']['street']}\n"
          f"numer lokalu: {datadict['address']['local_nb']}\n")
    json_d = json.dumps(datadict,indent=4)
    print(json_d)

except json.JSONDecodeError as e:
    print(f"błąd w parsowaniu: {e}")
