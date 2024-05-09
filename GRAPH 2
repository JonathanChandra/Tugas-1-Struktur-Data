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
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False
    
    def djikstra (self, source):
        #buat sebuah map yang melacak jarak dari setiap kota ke source
        distance = {}
        for city in self.cityList:
            distance[city] = float('inf')
        #tentukan jarak ke source = 0
        distance[source] = 0
        #buat sebuah sptSet
        
        unvisited_cities = []
        for city in self.cityList:
            unvisited_cities.append(city)
        
        #buat perulangan selama unvisited cities masih ada isinya
        while unvisited_cities:
            #buat variabel jarak minimum
            min_distance = float('inf')
            #buat variabel kota terdekat
            closest_city = None
            
            #cari kota terdekat dengan jarak minimum
            for city in unvisited_cities:
                #jika jarak kota lebih kecil daripada min distances
                if distance[city] < min_distance:
                #maka closest city dirubah ke kota tersebut
                    min_distance = distance[city]
                    closest_city = city
            
            #hapus vertex u dari unvisited
            unvisited_cities.remove(closest_city)
            
            #perbarui nilai jarak dari semua vertex yang berdekatan
            for neighbor, jarak in self.cityList[closest_city].items():
                #jika jarak kota terdekat + weight lebih kecil daripada jarak di distance, maka ubah nilai distance
                jarakNeighbor = distance[closest_city] + jarak
                if jarakNeighbor < distance[neighbor]:
                    distance[neighbor] = jarakNeighbor
        return distance
    

        
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
petaJawa.tambahkanJalan("Magelang","Salatiga", 49)
petaJawa.tambahkanJalan("Magelang","Wonogiri", 124)
petaJawa.tambahkanJalan("Magelang","Ngawi", 156)
petaJawa.tambahkanJalan("Magelang","Pacitan", 154)
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


print('------------------------------------------')
print('------------ PETA PULAU JAWA -------------')
jarakSemuaKotaDariMagelang = petaJawa.djikstra("Purwodadi")
print("Jarak kota berikut dari Purwodadi adalah :")
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
