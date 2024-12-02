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



except json.JSONDecodeError as e:
    print(f"błąd w parsowaniu: {e}")
