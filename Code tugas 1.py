class Node:
    def __init__(self, nama_menu, harga):
        self.nama_menu = nama_menu
        self.harga = harga
        self.next_node = None  # Perubahan nama dari 'next' ke 'next_node' untuk menghindari konflik dengan kata kunci 'next'

class LinkedList:
    def __init__(self):
        self.head = None # Linked list masih kosong (belum memiliki node apa pun)

    def add_order(self, nama_menu, harga):
        order_baru = Node(nama_menu, harga)
        if not self.head: # Memeriksa apakah self.head memiliki nilai atau tidak
            self.head = order_baru # Menambahkan order_baru menjadi node pertama dalam linked list
        else:
            # Inisialisasi variabel temp sebagai penanda untuk menelusuri linked list dari awal hingga akhir.
            temp = self.head
            # Temp akan merambat ke akhir
            while temp.next_node:
                temp = temp.next_node
            # Menambahkan node baru setelah node terakhir
            temp.next_node = order_baru

    def display_orders(self):
        temp = self.head
        while temp: # Selama temp memiliki nilai (tidak None)
            print(f"{temp.nama_menu} - {temp.harga}")  #Tampilkan nama menu dan harga dari node sekarang
            temp = temp.next_node # Perbarui temp untuk ke node berikutnya

    def calculate_total(self):
        total = 0
        temp = self.head
        while temp:
            total += temp.harga
            temp = temp.next_node
        return total



# Meminta input dari pengguna untuk memilih menu
while True:
    pilihan_menu = input("Silakan pilih menu (ketik 'selesai' untuk lanjut): ").strip()
    if pilihan_menu.lower() == 'selesai':
        break
    elif pilihan_menu in menu_miexue:
        jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
        tambah_pesanan(pilihan_menu, jumlah_pesanan)
    else:
        print("Menu tidak valid, silakan pilih menu yang tersedia.")    

tampilkan_pesanan()
hitung_total_harga()
