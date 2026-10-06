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
if input_panjang <= 0:
    print("Panjang harus lebih besar dari 0")
    exit()
input_lebar = int(input("Masukkan lebar persegi panjang: "))
if input_lebar <= 0:
    print("Lebar harus lebih besar dari 0")
    exit()

PP = PersegiPanjang(input_panjang, input_lebar)
print("keliling: ", PP.keliling())
print("luas: ", PP.luas())
print(PP.__str__())