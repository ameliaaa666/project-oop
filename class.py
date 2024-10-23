class Mobil:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def deskripsi (self):
        return f"{self.merk} {self.model} di buat pada tahun {self.tahun}."
    
Mobil = Mobil ("toyota","corolla",2020)
print(Mobil.deskripsi())