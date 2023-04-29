import os
from prettytable import PrettyTable
import pwinput
import time
os.system("cls")

def identitas():
    print("""
    ======================================================
    Kelompok 15 :   1. Adham Khautsar Leswono   2209116021
                    2. Aristy Avrianti          2209116027
                    3. Avinka Rizky             2209116049
    Tema        : Restaurant
    Prodi       : Sistem Informasi A'22
    ======================================================
    """)

# Lokasi file txt
invoice = "C:/Users/adham/Desktop/Praktikum_ASD/PA ASD/Invoice.txt"

# Nama user admin
admin = {"useradmin": ["admin"],
        "pwadmin": ["admin",]}

#Nama user pembeli
pembeli = {"userpembeli": ["adam", "aristy", "pinka"],
        "pwpembeli": ["123", "456", "789"]}

# Struktur data double linked list
class MenuItem:
    def __init__(self, name, price, prev_item=None, next_item=None):
        self.name = name
        self.price = price
        self.prev_item = prev_item
        self.next_item = next_item

class Menu:
    def __init__(self):
        self.food_head = None
        self.food_tail = None
        self.drink_head = None
        self.drink_tail = None

# Menambahkan item baru ke dalam menu
    def insert_item(self, category, name, price):
        new_item = MenuItem(name, price)

        if category == "food":
            head = self.food_head
            tail = self.food_tail
        elif category == "drink":
            head = self.drink_head
            tail = self.drink_tail

        if head is None:
            head = new_item
            tail = new_item
        else:
            tail.next_item = new_item
            new_item.prev_item = tail
            tail = new_item

        if category == "food":
            self.food_head = head
            self.food_tail = tail
        elif category == "drink":
            self.drink_head = head
            self.drink_tail = tail

# Menghapus item dari menu
    def remove_item(self, category, name):
        if category == "food":
            current_item = self.food_head
            tail = self.food_tail
        elif category == "drink":
            current_item = self.drink_head
            tail = self.drink_tail

        while current_item:
            if current_item.name == name:
                if current_item.prev_item:
                    current_item.prev_item.next_item = current_item.next_item
                else:
                    if category == "food":
                        self.food_head = current_item.next_item
                    elif category == "drink":
                        self.drink_head = current_item.next_item
                if current_item.next_item:
                    current_item.next_item.prev_item = current_item.prev_item
                else:
                    if category == "food":
                        self.food_tail = current_item.prev_item
                    elif category == "drink":
                        self.drink_tail = current_item.prev_item
                print(f"\t{name} BERHASIL DIHAPUS")
                time.sleep(1.5)
                os.system("cls")
                food_menu.display_menu("food")
                print("")
                print("="*30)
                x = input("'Enter'")
                menuadmin()
            current_item = current_item.next_item
        print(f"\t{name} TIDAK DITEMUKAN")
        time.sleep(1.5)
        menuadmin()

# Menampilkan menu
    def display_menu(self, category):
        if category == "food":
            head = self.food_head
        elif category == "drink":
            head = self.drink_head

        table = PrettyTable()
        table.field_names = ["Nama Item", "Harga"]
        current_item = head
        while current_item:
            table.add_row([current_item.name, f"Rp {current_item.price}"])
            current_item = current_item.next_item
        print("="*30)
        print(f"|         Menu {category.capitalize()}         |")
        print("="*30)
        print(table)

# Menu food
food_menu = Menu()
food_menu.insert_item("food", "Nasi Goreng", 15000)
food_menu.insert_item("food", "Mie Goreng", 8000)
food_menu.insert_item("food", "Ayam Goreng", 10000)
food_menu.insert_item("food", "Sate Ayam", 15000)
food_menu.insert_item("food", "Bakso", 13000)
food_menu.insert_item("food", "Tahu Goreng", 4000)
food_menu.insert_item("food", "Tempe Goreng", 4000)
food_menu.insert_item("food", "Nasi Putih", 4000)

# Menu drink
drink_menu = Menu()
drink_menu.insert_item("drink", "Es Teh Manis", 5000)
drink_menu.insert_item("drink", "Jus Jeruk", 7000)
drink_menu.insert_item("drink", "Kopi Hitam", 6000)
drink_menu.insert_item("drink", "Jus Alpukat", 10000)
drink_menu.insert_item("drink", "Teh Tarik", 6000)
drink_menu.insert_item("drink", "Redvelvet", 10000)
drink_menu.insert_item("drink", "Matcha", 10000)
drink_menu.insert_item("drink", "Air Mineral", 3000)

# Sortir menu merge sort
def merge_sort(menu_list, sort_key):
    if len(menu_list) <= 1:
        return menu_list
    
    middle = len(menu_list) // 2
    left = menu_list[:middle]
    right = menu_list[middle:]

    left = merge_sort(left, sort_key)
    right = merge_sort(right, sort_key)
    return merge(left, right, sort_key)
    
def merge(left, right, sort_key):
    result = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if sort_key == "favorite":
            if left[left_idx]["favorite"] < right[right_idx]["favorite"]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        elif sort_key == "price":
            if left[left_idx]["price"] < right[right_idx]["price"]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

    result += left[left_idx:]
    result += right[right_idx:]
    return result

# Sortir menu makanan berdasarkan harga
def mainfp():
    menu_food = [
        {"name": " Nasi Goreng", "price": 15000},
        {"name": " Mie Goreng", "price": 8000},
        {"name": " Ayam Goreng", "price": 10000},
        {"name": " Sate Ayam", "price": 15000},
        {"name": " Bakso    ", "price": 13000},
        {"name": " Tahu Goreng", "price": 4000},
        {"name": " Tempe Goreng", "price": 4000},
        {"name": " Nasi Putih", "price": 4000}
    ]
    sorted_menu_food = merge_sort(menu_food, "price")
    print("="*30)
    print("|      Sorted by Price      |")
    print("="*30)
    for menu in sorted_menu_food:
        print(menu["name"], "\t", ":", "Rp", menu["price"])
        print("="*30)

# Sortir menu makanan berdasarkan favorit
def mainff():
    menu_food = [
        {"name": " Nasi Goreng", "favorite": 3},
        {"name": " Mie Goreng", "favorite": 1},
        {"name": " Ayam Goreng", "favorite": 2},
        {"name": " Sate Ayam", "favorite": 7},
        {"name": " Bakso    ", "favorite": 4},
        {"name": " Tahu Goreng", "favorite": 6},
        {"name": " Tempe Goreng", "favorite": 8},
        {"name": " Nasi Putih", "favorite": 5}
    ]
    sorted_menu_food = merge_sort(menu_food, "favorite")
    print("="*30)
    print("|    Sorted by Top Seller    |")
    print("="*30)
    for menu in sorted_menu_food:
        print(menu["name"], "\t", ":", menu["favorite"])
        print("="*30)

# Sortir menu minuman berdasarkan harga
def maindp():
    menu_drink = [
        {"name": " Es Teh Manis", "price": 5000},
        {"name": " Jus Jeruk", "price": 7000},
        {"name": " Kopi Hitam", "price": 6500},
        {"name": " Jus Alpukat", "price": 11000},
        {"name": " Teh Tarik", "price": 7000},
        {"name": " Redvelvet", "price": 10000},
        {"name": " Matcha", "price": 10000},
        {"name": " Air Mineral", "price": 3000}
    ]
    sorted_menu_drink = merge_sort(menu_drink, "price")
    print("="*30)
    print("|      Sorted by Price      |")
    print("="*30)
    for menu in sorted_menu_drink:
        print(menu["name"], "\t", ":", "Rp", menu["price"])
        print("="*30)

# Sortir menu minuman berdasarkan favorit
def maindf():
    menu_drink = [
        {"name": " Es Teh Manis", "favorite": 1},
        {"name": " Jus Jeruk", "favorite": 3},
        {"name": " Kopi Hitam", "favorite": 5},
        {"name": " Jus Alpukat", "favorite": 4},
        {"name": " Teh Tarik", "favorite": 8},
        {"name": " Redvelvet", "favorite": 6},
        {"name": " Matcha", "favorite": 2},
        {"name": " Air Mineral", "favorite": 7}
    ]
    sorted_menu_drink = merge_sort(menu_drink, "favorite")
    print("="*30)
    print("|    Sorted by Top Seller    |")
    print("="*30)
    for menu in sorted_menu_drink:
        print(menu["name"], "\t", ":", menu["favorite"])
        print("="*30)

# Beli
class Order:
    def __init__(self):
        self.items = []
        self.total = 0

# Menambahkan item ke dalam list order
    def add_item(self, item):
        self.items.append(item)
        self.total += item.price

# Menampilkan menu dalam dalam opsi beli
def print_menu(menu):
    print("| No | Nama Item |   Harga   |")
    print("="*30)
    for item in menu:
        print(f"{item.name}\t : Rp {item.price}")
        print("="*30)

# Menampilkan list order dan total harga
def print_order(order):
    print("Order:")
    for item in order.items:
        print(f"  {item.name} : Rp {item.price}")
    print("="*10)
    print(f"Total: Rp {order.total}")

# Menu opsi beli
def main():
    menu_makanan = [
        MenuItem("1) Nasi Goreng ", 15000),
        MenuItem("2) Mie Goreng  ", 8000),
        MenuItem("3) Ayam Goreng ", 10000),
        MenuItem("4) Sate Ayam   ", 15000),
        MenuItem("5) Bakso       ", 13000),
        MenuItem("6) Tahu Goreng ", 4000),
        MenuItem("7) Tempe Goreng", 4000),
        MenuItem("8) Nasi Putih  ", 4000)
    ]

    menu_minuman = [
        MenuItem("1) Es Teh Manis", 5000),
        MenuItem("2) Jus Jeruk   ", 7000),
        MenuItem("3) Kopi Hitam  ", 6500),
        MenuItem("4) Jus Alpukat ", 11000),
        MenuItem("5) Teh Tarik   ", 7000),
        MenuItem("6) Redvelvet   ", 10000),
        MenuItem("7) Matcha      ", 10000),
        MenuItem("8) Air Mineral ", 3000)
    ]

    order = Order()
    while True:
        os.system("cls")
        print("="*30)
        print("|            Menu            |")
        print("="*30)
        print("1. Menu Food")
        print("2. Menu Drink")
        print("3. Kembali")
        print("4. Bayar")
        print("="*30)
        print_order(order)
        print("="*30)
        pilih = input("Pilih Opsi: ")
        if pilih == "1":
            os.system("cls")
            print("="*30)
            print("|         Food Menu         |")
            print("="*30)
            print_menu(menu_makanan)
            print("")
            print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN ORDER**")
            print("="*40)
            print("")
            choice = input("Masukkan No Menu: ")
            try:
                choice = int(choice)
            except ValueError:
                print("\tINPUTAN DATA TIDAK DITEMUKAN")
                time.sleep(1.5)
                continue
            if choice < 1 or choice > len(menu_makanan):
                print("\tINPUTAN DATA TIDAK DITEMUKAN")
                time.sleep(1.5)
            itemf = menu_makanan[choice - 1]
            order.add_item(itemf)
        elif pilih == "2":
            os.system("cls")
            print("="*30)
            print("|         Drink Menu         |")
            print("="*30)
            print_menu(menu_minuman)
            print("")
            print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN ORDER**")
            print("="*40)
            print("")
            pilih = input("Masukkan No Menu: ")
            try:
                pilih = int(pilih)
            except ValueError:
                print("\tINPUTAN DATA TIDAK DITEMUKAN")
                time.sleep(1.5)
                continue
            if pilih < 1 or pilih > len(menu_minuman):
                print("\tINPUTAN DATA TIDAK DITEMUKAN")
                time.sleep(1.5)
            itemm = menu_minuman[pilih - 1]
            order.add_item(itemm)
        elif pilih == "3":
            menupembeli()

    # Opsi transaksi
        elif pilih == "4":
            while True:
                os.system("cls")
                print("="*30)
                print("|     Metode Pembayaran     |")
                print("="*30)
                print("1. Tunai")
                print("2. Kembali")
                print("="*30)
                print_order(order)
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    os.system("cls")
                    print_order(order)
                    print("="*40)
                    bayar = input(" Masukkan Nominal Pembayaran: ")
                    try:
                        bayar = int(bayar)
                    except ValueError:
                        print("\tINPUTAN HANYA HARUS BERUPA ANGKA")
                        time.sleep(1.5)
                        break
                    if bayar < order.total:
                        print("\tUANG TIDAK CUKUP")
                        time.sleep(1.5)
                        break
                    elif order.total <= bayar:
                        kembalian = bayar - order.total
                        print("="*40)
                        time.sleep(1)
                        print(". . . . . . . . . . . . . . . . . . . .")
                        time.sleep(1)
                        print(". . . . . . . . . . . . . . . . . . . .")
                        time.sleep(1)
                        print(". . . . . . . . . . . . . . . . . . . .")
                        time.sleep(1)
                    with open (invoice,"a") as save:
                        print("", file = save)
                        print("<"*19, ">"*19, file = save)
                        print(" STRUK BELANJA ".center(40,"="), file = save)
                        print("<"*19, ">"*19, file = save)
                        print(" Restaurant ".center(40,"="), file = save)
                        for item in order.items:
                            print(f" {item.name}\t    : Rp {item.price}", file = save)
                        print("", file = save)
                        print("        ","<"*10, ">"*10, file = save)
                        print(f" Total Pembayaran\t    : Rp {order.total}", file = save)
                        print(" Tunai\t                : Rp", bayar, file = save)
                        print(" Kembalian\t            : Rp", kembalian, file = save)
                        print(40*"=", file = save)                    
                        print(" THANK YOU FOR YOUR ORDER ".center(40,"="), file = save)
                        print(" KAMI TUNGGU KEDATANGANNYA KEMBALI ".center(40,"="), file = save)
                        print(40*"=", file = save)
                    os.system("cls")
                    print("<"*19, ">"*19)
                    print(" STRUK BELANJA ".center(40,"="))
                    print("<"*19, ">"*19)
                    print(" Restaurant ".center(40,"="))
                    for item in order.items:
                        print(f" {item.name}\t: Rp {item.price}")
                    print("")
                    print("        ","<"*10, ">"*10)
                    print(f" Total Pembayaran\t: Rp {order.total}")
                    print(" Tunai\t                : Rp", bayar)
                    print(" Kembalian\t        : Rp", kembalian)
                    print(40*"=")                    
                    print(" THANK YOU FOR YOUR ORDER ".center(40,"="))
                    print(" KAMI TUNGGU KEDATANGANNYA KEMBALI ".center(40,"="))
                    print(40*"=")
                    print("")
                    print("="*30)
                    x = input("'Enter'")
                    menupembeli()
                elif pilih == "2":
                    break
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)
        elif all(i.isspace() for i in pilih):
            print("\tINPUTAN DATA KOSONG")
            time.sleep(1.5)
        else:
            print("\tINPUTAN DATA SALAH")
            time.sleep(1.5)

# Tampilan utama
def utama():
    while True:
        try:
            os.system("cls")
            identitas() 
            print ("Silahkan Tentukan Pilihan Anda :\n1. Login Admin\n2. Login Pembeli\n3. Keluar Program")
            print("="*40)
            pilih = input("Tentukan Pilihan: ")

        # Login admin
            if pilih == "1":
                while True:
                    os.system("cls")
                    ua = input("Input Username: ")
                    pwa = pwinput.pwinput(prompt = "Input Password: ")
                    try:
                        log1 = admin.get("useradmin").index(ua)
                        if ua == admin.get("useradmin")[log1] and pwa == admin.get("pwadmin")[log1]:
                            print("")
                            print("="*30)
                            print("|       LOGIN BERHASIL       |")
                            print("="*30)
                            time.sleep(1.5)
                            menuadmin()
                        else:
                            print("\tPASSWORD SALAH")
                            time.sleep(1.5)
                            utama()
                    except:
                        time.sleep(1.5)        
                        break

        # Login pembeli
            elif pilih == "2":
                while True:
                    os.system("cls")
                    up = input("Input Username: ")
                    pwp = pwinput.pwinput(prompt = "Input Password: ")
                    try:
                        log1 = pembeli.get("userpembeli").index(up)
                        if up == pembeli.get("userpembeli")[log1] and pwp == pembeli.get("pwpembeli")[log1]:
                            print("")
                            print("="*30)
                            print("|       LOGIN BERHASIL       |")
                            print("="*30)
                            time.sleep(1.5)
                            os.system("cls")
                            print("="*30)
                            print("|       SELAMAT DATANG       |")
                            print("="*30)
                            time.sleep(1.5)
                            menupembeli()
                        elif up == pembeli.get("userpembeli")[log1] and pwp != pembeli.get("pwpembeli")[log1]:
                            print("\tPASSWORD SALAH")
                            time.sleep(1.5)
                            utama()
                        elif up == pembeli.get("userpembeli")[log2] and pwp == pembeli.get("pwpembeli")[log2]:
                            print("")
                            print("="*30)
                            print("|       LOGIN BERHASIL       |")
                            print("="*30)
                            time.sleep(1.5)
                            os.system("cls")
                            print("="*30)
                            print("|       SELAMAT DATANG       |")
                            print("="*30)
                            time.sleep(1.5)
                            menupembeli()
                        elif up == pembeli.get("userpembeli")[log2] and pwp != pembeli.get("pwpembeli")[log2]:
                            print("\tPASSWORD SALAH")
                            time.sleep(1.5)
                            utama()
                        elif up == pembeli.get("userpembeli")[log3] and pwp == pembeli.get("pwpembeli")[log3]:
                            print("")
                            print("="*30)
                            print("|       LOGIN BERHASIL       |")
                            print("="*30)
                            time.sleep(1.5)
                            os.system("cls")
                            print("="*30)
                            print("|       SELAMAT DATANG       |")
                            print("="*30)
                            time.sleep(1.5)
                            menupembeli()
                        elif up == pembeli.get("userpembeli")[log3] and pwp != pembeli.get("pwpembeli")[log3]:
                            print("\tPASSWORD SALAH")
                            time.sleep(1.5)
                            utama()
                    except:
                        time.sleep(1.5)        
                        break

        # End program
            elif pilih == "3":
                print("\tPROGRAM SELESAI")
                time.sleep(1.5)
                os.system("cls")
                print("<"*23, ">"*24)
                print(" Restaurant ".center(48,"="))
                print(" TERIMA KASIH TELAH BERKUNJUNG DISINI ".center(48,"="))
                print("<"*23, ">"*24)
                time.sleep(1.5)
                raise SystemExit
            elif all(i.isspace() for i in pilih):
                print("\tINPUTAN DATA KOSONG")
                time.sleep(1.5)
            else:
                print("\tINPUTAN DATA SALAH")
                time.sleep(1.5)
        except:
            raise SystemExit

# Tampilan menu pembeli
def menuadmin():
    while True:
        os.system("cls")
        print("="*30)
        print("|         Restaurant         |")
        print("="*30)
        print("1. Tampilkan Menu")
        print("2. Cari Menu")
        print("3. Sortir Menu")
        print("4. Tambah Menu")
        print("5. Hapus Menu")
        print("6. Kembali Tampilan Utama")
        print("="*30)
        pilih = input("Pilih Opsi: ")
        if pilih == "1":
            while True:
                os.system("cls")
                print("="*30)
                print("|       Tampilkan Menu       |")
                print("="*30)
                print("1. Menu Food")
                print("2. Menu Drink")
                print("3. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    os.system("cls")
                    food_menu.display_menu("food")
                    print("")
                    print("="*30)
                    x = input("'Enter'")
                    menuadmin()
                elif pilih == "2":
                    os.system("cls")
                    drink_menu.display_menu("drink")
                    print("")
                    print("="*30)
                    x = input("'Enter'")
                    menuadmin()
                elif pilih == "3":
                    menuadmin()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)

    # Mencari item dalam menu
        elif pilih == "2":
            while True:
                os.system("cls")
                print("="*30)
                print("|         Cari Menu          |")
                print("="*30)
                print("1. Lanjutkan Pencarian")
                print("2. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    os.system("cls")
                    print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN PENCARIAN**")
                    print("="*40)
                    print("")

                # Jump search
                    query = input("Masukkan Nama Menu: ")
                    found = False
                    for category in ["food", "drink"]:
                        if category == "food":
                            head = food_menu.food_head
                        elif category == "drink":
                            head = drink_menu.drink_head
                        current_item = head
                        while current_item:
                            if query.lower() in current_item.name.lower():
                                if not found:
                                    table = PrettyTable()
                                    table.field_names = ["Nama Item", "Harga"]
                                found = True
                                table.add_row([current_item.name, f"Rp {current_item.price}"])
                            current_item = current_item.next_item
                    if all(i.isspace() for i in query):
                        print("\tINPUTAN DATA KOSONG")
                        time.sleep(1.5)
                    elif found:
                        time.sleep(1.5)
                        print("")
                        print(f"Hasil Pencarian Untuk '{query}':")
                        print("\t"), print(table)
                        print("")
                        print("="*30)
                        x = input("'Enter'")
                        continue
                    else:
                        time.sleep(1.5)
                        print("")
                        print(f"Hasil Pencarian Untuk '{query}':\n\tTIDAK DITEMUKAN")
                        print("")
                        print("="*30)
                        x = input("'Enter'")
                        continue
                elif pilih == "2":
                    menuadmin()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)
        elif pilih == "3":
            while True:
                os.system("cls")
                print("="*30)
                print("|        Sortir Menu        |")
                print("="*30)
                print("1. Menu Food")
                print("2. Menu Drink")
                print("3. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    while True:
                        os.system("cls")
                        print("="*30)
                        print("|         Food Menu         |")
                        print("="*30)
                        print("1. Ter-Murah")
                        print("2. Ter-Favorit")
                        print("3. Kembali")
                        print("="*30)
                        pilih = input("Pilih Opsi: ")
                        if pilih == "1":
                            os.system("cls")
                            mainfp()
                            print("")
                            x = input("'Enter'")
                            menuadmin()
                        elif pilih == "2":
                            os.system("cls")
                            mainff()
                            print("")
                            x = input("'Enter'")
                            menuadmin()
                        elif pilih == "3":
                            break
                        elif all(i.isspace() for i in pilih):
                            print("\tINPUTAN DATA KOSONG")
                            time.sleep(1.5)
                        else:
                            print("\tINPUTAN DATA SALAH")
                            time.sleep(1.5)
                elif pilih == "2":
                    while True:
                        os.system("cls")
                        print("="*30)
                        print("|         Drink Menu         |")
                        print("="*30)
                        print("1. Ter-Murah")
                        print("2. Ter-Favorit")
                        print("3. Kembali")
                        print("="*30)
                        pilih = input("Pilih Opsi: ")
                        if pilih == "1":
                            os.system("cls")
                            maindp()
                            print("")
                            x = input("'Enter'")
                            menuadmin()
                        elif pilih == "2":
                            os.system("cls")
                            maindf()
                            print("")
                            x = input("'Enter'")
                            menuadmin()
                        elif pilih == "3":
                                break
                        elif all(i.isspace() for i in pilih):
                            print("\tINPUTAN DATA KOSONG")
                            time.sleep(1.5)
                        else:
                            print("\tINPUTAN DATA SALAH")
                            time.sleep(1.5)
                elif pilih == "3":
                    menuadmin()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)
        elif pilih == "4":
            while True:
                os.system("cls")
                print("="*30)
                print("|        Tambah Menu         |")
                print("="*30)
                print("1. Menu Food")
                print("2. Menu Drink")
                print("3. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")

            # Menambahkan item pada menu food
                if pilih == "1":
                    os.system("cls")
                    food_menu.display_menu("food")
                    print("")
                    print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN PERUBAHAN**")
                    print("="*40)
                    print("")
                    name = input("Masukkan Nama Menu Baru: ")
                    if all(i.isspace() for i in name):
                        print("\tINPUTAN DATA KOSONG")
                        time.sleep(1.5)
                        menuadmin()
                    else:
                        price = input("Masukkan Harga Menu Baru: ")
                        if all(i.isspace() for i in price):
                            print("\tINPUTAN DATA KOSONG")
                            time.sleep(1.5)
                            menuadmin()
                        elif all(not i.isdigit() for i in price):
                            print("\tHARGA HARUS BERUPA ANGKA")
                            time.sleep(1.5)
                            menuadmin()
                    food_menu.insert_item("food", name, int(price))
                    print(f"\t{name} BERHASIL DITAMBAHKAN")
                    time.sleep(1.5)
                    os.system("cls")
                    food_menu.display_menu("food")
                    print("")
                    print("="*30)
                    x = input("'Enter'")
                    menuadmin()

            # Menambahkan item pada menu drink
                elif pilih == "2":
                    os.system("cls")
                    drink_menu.display_menu("drink")
                    print("")
                    print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN PERUBAHAN**")
                    print("="*40)
                    print("")
                    name = input("Masukkan Nama Menu Baru: ")
                    if all(i.isspace() for i in name):
                        print("\tINPUTAN DATA KOSONG")
                        time.sleep(1.5)
                        menuadmin()
                    else:
                        price = input("Masukkan Harga Menu Baru: ")
                        if all(i.isspace() for i in price):
                            print("\tINPUTAN DATA KOSONG")
                            time.sleep(1.5)
                            menuadmin()
                        elif all(not i.isdigit() for i in price):
                            print("\tHARGA HARUS BERUPA ANGKA")
                            time.sleep(1.5)
                            menuadmin()
                    drink_menu.insert_item("drink", name, int(price))
                    print(f"\t{name} BERHASIL DITAMBAHKAN")
                    time.sleep(1.5)
                    os.system("cls")
                    drink_menu.display_menu("drink")
                    print("")
                    print("="*30)
                    x = input("'Enter'")
                    menuadmin()
                elif pilih == "3":
                    menuadmin()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)
        elif pilih == "5":
            while True:
                os.system("cls")
                print("="*30)
                print("|        Hapus Menu          |")
                print("="*30)
                print("1. Menu Food")
                print("2. Menu Drink")
                print("3. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    os.system("cls")
                    food_menu.display_menu("food")
                    print("")
                    print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN PERUBAHAN**")
                    print("="*40)
                    print("")
                    name = input("Masukkan Nama Menu Yang Ingin Dihapus: ")
                    if all(i.isspace() for i in name):
                        print("\tINPUTAN DATA KOSONG")
                        time.sleep(1.5)
                        menuadmin()
                    food_menu.remove_item("food", name)
                elif pilih == "2":
                    os.system("cls")
                    drink_menu.display_menu("drink")
                    print("")
                    print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN PERUBAHAN**")
                    print("="*40)
                    print("")
                    name = input("Masukkan Nama Menu Yang Ingin Dihapus: ")
                    if all(i.isspace() for i in name):
                        print("\tINPUTAN DATA KOSONG")
                        time.sleep(1.5)
                        menuadmin()
                    drink_menu.remove_item("drink", name)
                elif pilih == "3":
                    menuadmin()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)
        elif pilih == "6":
            raise SystemExit
        elif all(i.isspace() for i in pilih):
            print("\tINPUTAN DATA KOSONG")
            time.sleep(1.5)
        else:
            print("\tINPUTAN DATA SALAH")
            time.sleep(1.5)

# Tampilan menu pembeli
def menupembeli():
    while True:
        os.system("cls")
        print("="*30)
        print("|         Restaurant         |")
        print("="*30)
        print("1. Tampilkan Menu")
        print("2. Cari Menu")
        print("3. Sortir Menu")
        print("4. Beli")
        print("5. Kembali Tampilan Utama")
        print("="*30)
        pilih = input("Pilih Opsi: ")
        if pilih == "1":
            while True:
                os.system("cls")
                print("="*30)
                print("|       Tampilkan Menu       |")
                print("="*30)
                print("1. Menu Food")
                print("2. Menu Drink")
                print("3. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    os.system("cls")
                    food_menu.display_menu("food")
                    print("")
                    print("="*30)
                    x = input("'Enter'")
                    menupembeli()
                elif pilih == "2":
                    os.system("cls")
                    drink_menu.display_menu("drink")
                    print("")
                    print("="*30)
                    x = input("'Enter'")
                    menupembeli()
                elif pilih == "3":
                    menupembeli()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)

    # Mencari item dalam menu
        elif pilih == "2":
            while True:
                os.system("cls")
                print("="*30)
                print("|         Cari Menu          |")
                print("="*30)
                print("1. Lanjutkan Pencarian")
                print("2. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    os.system("cls")
                    print("**KOSONGKAN INPUTAN UNTUK MEMBATALKAN PENCARIAN**")
                    print("="*40)
                    print("")

                # Jump search
                    query = input("Masukkan Nama Menu: ")
                    found = False
                    for category in ["food", "drink"]:
                        if category == "food":
                            head = food_menu.food_head
                        elif category == "drink":
                            head = drink_menu.drink_head
                        current_item = head
                        while current_item:
                            if query.lower() in current_item.name.lower():
                                if not found:
                                    table = PrettyTable()
                                    table.field_names = ["Nama Item", "Harga"]
                                found = True
                                table.add_row([current_item.name, f"Rp {current_item.price}"])
                            current_item = current_item.next_item
                    if all(i.isspace() for i in query):
                        print("\tINPUTAN DATA KOSONG")
                        time.sleep(1.5)
                    elif found:
                        time.sleep(1.5)
                        print("")
                        print(f"Hasil Pencarian Untuk '{query}':")
                        print("\t"), print(table)
                        print("")
                        print("="*30)
                        x = input("'Enter'")
                        continue
                    else:
                        time.sleep(1.5)
                        print("")
                        print(f"Hasil Pencarian Untuk '{query}':\n\tTIDAK DITEMUKAN")
                        print("")
                        print("="*30)
                        x = input("'Enter'")
                        continue
                elif pilih == "2":
                    menupembeli()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)
        elif pilih == "3":
            while True:
                os.system("cls")
                print("="*30)
                print("|        Sortir Menu        |")
                print("="*30)
                print("1. Menu Food")
                print("2. Menu Drink")
                print("3. Kembali")
                print("="*30)
                pilih = input("Pilih Opsi: ")
                if pilih == "1":
                    while True:
                        os.system("cls")
                        print("="*30)
                        print("|         Food Menu         |")
                        print("="*30)
                        print("1. Ter-Murah")
                        print("2. Ter-Favorit")
                        print("3. Kembali")
                        print("="*30)
                        pilih = input("Pilih Opsi: ")
                        if pilih == "1":
                            os.system("cls")
                            mainfp()
                            print("")
                            x = input("'Enter'")
                            menupembeli()
                        elif pilih == "2":
                            os.system("cls")
                            mainff()
                            print("")
                            x = input("'Enter'")
                            menupembeli()
                        elif pilih == "3":
                                break
                        elif all(i.isspace() for i in pilih):
                            print("\tINPUTAN DATA KOSONG")
                            time.sleep(1.5)
                        else:
                            print("\tINPUTAN DATA SALAH")
                            time.sleep(1.5)
                elif pilih == "2":
                    while True:
                        os.system("cls")
                        print("="*30)
                        print("|         Drink Menu         |")
                        print("="*30)
                        print("1. Ter-Murah")
                        print("2. Ter-Favorit")
                        print("3. Kembali")
                        print("="*30)
                        pilih = input("Pilih Opsi: ")
                        if pilih == "1":
                            os.system("cls")
                            maindp()
                            print("")
                            x = input("'Enter'")
                            menupembeli()
                        elif pilih == "2":
                            os.system("cls")
                            maindf()
                            print("")
                            x = input("'Enter'")
                            menupembeli()
                        elif pilih == "3":
                                break
                        elif all(i.isspace() for i in pilih):
                            print("\tINPUTAN DATA KOSONG")
                            time.sleep(1.5)
                        else:
                            print("\tINPUTAN DATA SALAH")
                            time.sleep(1.5)
                elif pilih == "3":
                    menupembeli()
                elif all(i.isspace() for i in pilih):
                    print("\tINPUTAN DATA KOSONG")
                    time.sleep(1.5)
                else:
                    print("\tINPUTAN DATA SALAH")
                    time.sleep(1.5)

    # Opsi beli
        elif pilih == "4":
            main()
        elif pilih == "5":
            raise SystemExit
        elif all(i.isspace() for i in pilih):
            print("\tINPUTAN DATA KOSONG")
            time.sleep(1.5)
        else:
            print("\tINPUTAN DATA SALAH")
            time.sleep(1.5)

utama()