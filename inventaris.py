import json
path = r"C:\Users\Hype AMD\Downloads\DDP\StudiKasusDDP01\barang.json"

with open(path,"r", encoding="utf-8") as f:
    data = json.load(f)

def tambah_data(nama, kode, stok, harga):
    data.append({
        "nama" : nama,
        "kode" : kode,
        "stok" : stok,
        "harga" : harga
    })

    return "Data ditambah"

def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

while True:
    print("Menu Sistem Manajemen Inventaris Barang")
    print("1. Lihat semua barang")
    print("2. Tambah barang baru")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        print("data awal")
        print(data)
    elif pilihan == '2':
        nama = input("Masukkan nama barang baru: ")
        kode = input("Masukkan kode barang: ")
        stok = input("Masukkan stok barang: ")
        harga = input("Masukkan harga barang: ")
        tambah_data(nama, kode, stok, harga)
        simpan_file()
        print("Berhasil menambah barang!")
    else:
        pilihan == '3'
        print("Keluar dari menu")
        break