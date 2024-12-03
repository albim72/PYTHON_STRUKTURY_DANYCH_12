import csv

with open("firma.csv",encoding="utf-8") as pc:
    csv_reader = csv.reader(pc,delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"nazwa kolumny: {', '.join(row)}")
            line_count += 1
        else:
            print(f"\t{row[0]} pracuje na stanowisku: {row[1]} i ma urodziny "
                  f"w miesiącu {row[2]}. Otrzymuje nagrodę finansową w wysokości: {row[3]} zł")
            line_count += 1

    print("_"*50)
    print(f"dodano {line_count} linii")
    print(f"dodano {line_count-1} osób")

print("Jak utworzyć nowy plik CSV?")

dane = [
        ['Karol','Kret','Finanse',10],
        ['Olga','Nowik','IT',7],
        ['Leon','Kos','Finanse',3],
        ['Daria','Kłos','IT',11],
        ['Jan','Kowal','Marketing',5]
    ]

with open("pracownik.csv","w",encoding="utf-8", newline="") as ef:
    emp_writer = csv.writer(ef,delimiter=",",quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
    emp_writer.writerows(dane)

with open("pracownik.csv",encoding="utf-8") as g:
    csv_reader = csv.reader(g,delimiter=",")
    for r in csv_reader:
        print(f"Dane: {', '.join(r)}")
