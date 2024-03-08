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
        while temp: # "Selama temp memiliki nilai (tidak None)
            print(f"{temp.nama_menu} - {temp.harga}")  #Tampilkan nama menu dan harga dari node sekarang
            temp = temp.next_node # Perbarui temp untuk ke node berikutnya

    def calculate_total(self):
        total = 0
        temp = self.head
        while temp:
            total += temp.harga
            temp = temp.next_node
        return total

# Inisialisasi linked list untuk pesanan Miexue
pesanan_miexue = LinkedList()

# Menu Miexue
menu_miexue = {
    "Miexue Ice Cream": 5000,
    "Boba Shake": 16000,
    "Mi Sundae": 14000,
    "Mi Ganas": 11000,
    "Creamy Mango Boba": 22000
}

# Menampilkan semua menu
def tampilkan_menu():
    print("Daftar Menu:")
    for menu, harga in menu_miexue.items():
        print(f"{menu} - {harga} Rupiah")

# Menambah pesanan ke keranjang
def tambah_pesanan(menu, jumlah):
    for _ in range(jumlah):
        pesanan_miexue.add_order(menu, menu_miexue[menu])
    print(f"{jumlah} {menu} telah ditambahkan ke keranjang.")

# Menampilkan pesanan yang sudah ditambahkan
def tampilkan_pesanan():
    print("Pesanan Anda:")
    pesanan_miexue.display_orders()

# Menghitung jumlah harga yang dibayarkan
def hitung_total_harga():
    total_harga = pesanan_miexue.calculate_total()
    print(f"Total harga yang harus dibayarkan: {total_harga} Rupiah.")

# Menampilkan semua menu saat program dimulai
tampilkan_menu()

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
