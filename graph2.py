from itertools import permutations

class Peta:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
            for neighbor, distance in self.cityList[kota].items():
                print("    ->", neighbor,":",distance)
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = {}
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.cityList:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.cityList[kotalain]:
                    del self.cityList[kotalain][kotaDihapus]
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2,jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2][kota1] = jarak
            #masukkan kota 2 di list kota1
            self.cityList[kota1][kota2] = jarak
            return True
        return False
    
    
    

        
petaJawa = Peta()
petaJawa.tambahkanKota("Magelang")
petaJawa.tambahkanKota("Salatiga")
petaJawa.tambahkanKota("Wonogiri")
petaJawa.tambahkanKota("Purwodadi")
petaJawa.tambahkanKota("Ngawi")
petaJawa.tambahkanKota("Bojonegoro")
petaJawa.tambahkanKota("Tuban")
petaJawa.tambahkanKota("Madiun")
petaJawa.tambahkanKota("Ponorogo")
petaJawa.tambahkanKota("Pacitan")
petaJawa.tambahkanKota("Nganjuk")
petaJawa.tambahkanKota("Kediri")
petaJawa.tambahkanJalan("Purwodadi","Wonogiri", 104)
petaJawa.tambahkanJalan("Purwodadi","Tuban", 149)
petaJawa.tambahkanJalan("Purwodadi","Bojonegoro", 127)
petaJawa.tambahkanJalan("Purwodadi","Ngawi", 91)
petaJawa.tambahkanJalan("Purwodadi","Nganjuk", 156)
petaJawa.tambahkanJalan("Salatiga","Purwodadi", 67)
petaJawa.tambahkanJalan("Salatiga","Ngawi", 118)
petaJawa.tambahkanJalan("Ponorogo","Purwodadi", 140)
petaJawa.tambahkanJalan("Kediri","Purwodadi", 208)
petaJawa.tambahkanJalan("Madiun","Purwodadi", 124)
petaJawa.tambahkanJalan("Magelang","Salatiga", 49)
petaJawa.tambahkanJalan("Magelang","Wonogiri", 124)
petaJawa.tambahkanJalan("Magelang","Ngawi", 156)
petaJawa.tambahkanJalan("Magelang","Pacitan", 154)
petaJawa.tambahkanJalan("Magelang","Purwodadi", 111)
petaJawa.tambahkanJalan("Magelang","Bojonegoro", 232)
petaJawa.tambahkanJalan("Magelang","Tuban", 270)
petaJawa.tambahkanJalan("Magelang","Madiun", 192)
petaJawa.tambahkanJalan("Magelang","Nganjuk", 222)
petaJawa.tambahkanJalan("Magelang","Kediri", 272)
petaJawa.tambahkanJalan("Magelang","Ponorogo", 177)
petaJawa.tambahkanJalan("Nganjuk","Magelang", 222)
petaJawa.tambahkanJalan("Nganjuk","Salatiga", 182)
petaJawa.tambahkanJalan("Nganjuk","Purwodadi", 156)
petaJawa.tambahkanJalan("Nganjuk","Wonogiri", 146)
petaJawa.tambahkanJalan("Nganjuk","Ngawi", 64)
petaJawa.tambahkanJalan("Nganjuk","Madiun", 50)
petaJawa.tambahkanJalan("Nganjuk","Pacitan", 157)
petaJawa.tambahkanJalan("Nganjuk","Tuban", 102)
petaJawa.tambahkanJalan("Nganjuk","Bojonegoro", 64)
petaJawa.tambahkanJalan("Nganjuk","Ponorogo", 79)
petaJawa.tambahkanJalan("Nganjuk","Kediri", 53)


print('------------------------------------------')
print('------------ PETA PULAU JAWA -------------')
jarakSemuaKotaDariMagelang = petaJawa.djikstra("Nganjuk")
print("Jarak kota berikut dari Nganjuk adalah :")
for city,distance in jarakSemuaKotaDariMagelang.items():
    print(city," adalah ",distance," KM")
    
jawa = ["Magelang","Salatiga","Wonogiri"]
print(permutations(jawa))
print('------------------------------------------')
print('-------------- KELOMPOK 4 ----------------')
print('M. MARDLIAN NUROFIQ')
print('JONATHAN CHANDRA IVANTA')
print('RADITYA BANI')
print('------------------------------------------')
