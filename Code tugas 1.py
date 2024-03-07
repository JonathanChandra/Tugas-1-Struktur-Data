class Node:
    def __init__(self, nama_menu, harga):
        self.nama_menu = nama_menu
        self.harga = harga
        self.next_node = None  # Perubahan nama dari 'next' ke 'next_node' untuk menghindari konflik dengan kata kunci 'next'

class LinkedList:
    def __init__(self):
        self.head = None

    def add_order(self, nama_menu, harga):
        order_baru = Node(nama_menu, harga)
        if not self.head:
            self.head = order_baru
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = order_baru

    def display_orders(self):
        current = self.head
        while current:
            print(f"{current.nama_menu} - {current.harga}")
            current = current.next_node

    def calculate_total(self):
        total = 0
        current = self.head
        while current:
            total += current.price
            current = current.next_node
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

# Fungsi untuk menambah pesanan ke keranjang
def tambah_pesanan(menu, jumlah):
    for _ in range(jumlah):
        miexue_orders.add_order(menu, menu_miexue[menu])
    print(f"{jumlah} {menu} telah ditambahkan ke keranjang.")

# Fungsi untuk menampilkan pesanan yang sudah ditambahkan
def tampilkan_pesanan():
    print("Pesanan Anda:")
    miexue_orders.display_orders()

# Fungsi untuk menghitung jumlah harga yang dibayarkan
def hitung_total_harga():
    total_harga = miexue_orders.calculate_total()
    print(f"Total harga yang harus dibayarkan: {total_harga} Rupiah.")

# Contoh penggunaan
tambah_pesanan("Miexue Ice Cream", 2)
tambah_pesanan("Boba Shake", 1)
tambah_pesanan("Mi Sundae", 3)

tampilkan_pesanan()
hitung_total_harga()
