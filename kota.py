class Peta:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.cityList:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False
        

petaJawa = Peta()
petaJawa.tambahkanKota("Magelang")
petaJawa.tambahkanKota("Salatiga")
petaJawa.tambahkanKota("Wonogiri")
petaJawa.tambahkanKota("Purwodadi")
petaJawa.tambahkanKota("Ngawi")
petaJawa.tambahkanKota("Purwodadi")
petaJawa.tambahkanKota("Bojonegoro")
petaJawa.tambahkanKota("Tuban")
petaJawa.tambahkanJalan("Magelang","Salatiga")
petaJawa.tambahkanJalan("Salatiga","Wonogiri")
petaJawa.tambahkanJalan("Magelang","Wonogiri")
petaJawa.tambahkanJalan("Purwodadi","Wonogiri")
petaJawa.tambahkanJalan("Purwodadi","Tuban")
petaJawa.tambahkanJalan("Purwodadi","Bojonegoro")
petaJawa.tambahkanJalan("Purwodadi","Ngawi")
petaJawa.tambahkanJalan("Ngawi","Bojonegoro")
petaJawa.tambahkanJalan("Tuban","Bojonegoro")
petaJawa.tambahkanJalan("Wonogiri","Ngawi")
petaJawa.tambahkanJalan("Magelang","Ngawi")
petaJawa.printPeta()
print('------------------------------')
petaJawa.hapusKota("wonogiri")
petaJawa.printPeta()
