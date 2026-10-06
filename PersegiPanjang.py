class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def __str__(self):
        return f"Persegi Panjang dengan panjang {self.panjang} dan lebar {self.lebar}"
    
input_panjang = int(input("Masukkan panjang persegi panjang: "))
input_lebar = int(input("Masukkan lebar persegi panjang: "))