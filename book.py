class Book:
    wydawnictwo:str

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self._oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return f"Książka -> {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self._oprawa}"

    def __call__(self,rabat):
        print(f"Rabat {rabat} % = {self.cena*(rabat/100)} zł")

    def create_book(self):
        print("utworzenie nowej książki!")

bk1 = Book(34,"ABC kulturysty","Jan Kowal",67)
print(bk1)
bk1(12)
