class eiger:
    def __init__(self, jenis, warna, kapasitas):
        self.jenis = jenis
        self.warna = warna
        self.kapasitas = kapasitas

    def printname(self):
        print(self.jenis)
        print(self.warna)
        print(self.kapasitas)

class Daypack(eiger):
     def __init__(self, jenis, warna, kapasitas):
         eiger.__init__(self, jenis, warna, kapasitas)
         self.harga = "Rp. 350.000"

     def Daypack(Self):
        print("Jenis            : ", Self.jenis)
        print("Warna            : ", Self.warna)
        print("Kapasitas        : ", Self.kapasitas)
        print("Harga            : ", Self.harga)


class Carrier(eiger):
    def __init__(self, jenis, warna, kapasitas):
          eiger.__init__(self, jenis, warna, kapasitas)
          self.harga = "Rp. 1.000.000"

    def Carrier(Self):
        print("Jenis            : ", Self.jenis)
        print("Warna            : ", Self.warna)
        print("Kapasitas        : ", Self.kapasitas)
        print("Harga            : ", Self.harga)

class Slingbag(eiger):
     def __init__(self, jenis, warna, kapasitas):
         eiger.__init__(self, jenis, warna, kapasitas)
         self.harga = "Rp. 200.000"

     def Slingbag(Self):
        print("Jenis            : ", Self.jenis)
        print("Warna            : ", Self.warna)
        print("Kapasitas        : ", Self.kapasitas)
        print("Harga            : ", Self.harga)


x = Daypack("Eiger Daypack", "Army", "15 liter")
y = Carrier("Eiger Carrier", "Orange", "35 liter")
z = Slingbag("Eiger sling bag", "Biru", "2 liter")

print ("=========================================")
x.Daypack()
print ("=========================================")
y.Carrier()
print ("=========================================")
z.Slingbag()
print ("=========================================")