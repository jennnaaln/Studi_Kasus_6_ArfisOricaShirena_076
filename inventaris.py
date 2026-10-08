import json # mengimpor modul python bawaan untuk mengolah file json
path = r"C:\Users\Hype AMD\Downloads\DDP\StudiKasusDDP01\barang.json" # menyimpan lokasi/alamat file barang.json ke dalam komputer 

(saya menggunakan path soalnya kalau pake nama file barang.json langsung, terjadi error)

with open(path,"r", encoding="utf-8") as f: # membaca isi file barang.json
    data = json.load(f)

def tambah_data(nama, kode, stok, harga): # menambahkan data barang baru berupa dictionary, data baru akan masuk ke daftar list di file barang.json. 
    # def atau function berfungsi untuk menerima input nama, kode, stok dan harga barang
    data.append({ # data barang baru akan tertambah dan akan tersimpan ke dalam file json
        "nama" : nama,
        "kode" : kode,
        "stok" : stok,
        "harga" : harga
    })

    return "Data ditambah"

def simpan_file(): # menuliskan kembali seluruh isi variabel data yang sudah tambah atau diperbarui ke dalam file barang.json agar perubahan tersimpan secara permanen
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4) # indent = 4 digunakan agar format json rapi dan mudah dibaca

while True: # digunakan agar program jalan terus menerus 
    print("Menu Sistem Manajemen Inventaris Barang")
    print("1. Lihat semua barang") # menampilkan seluruh data barang yang telah diinput atau yang saat ini tersimpan di file barang.json 
    print("2. Tambah barang baru") # mengambil input dari pengguna berupa nama, kode, stok dan harga barang. lalu data baru tersebut tersimpan ke dalam file dengan fungsi simpan_file() 
    print("3. Keluar") # menghentikan perulangan program dengan perintah break

    pilihan = input("Pilih menu: ") # akan menampilkan teks "pilih menu" di layar dan menerima input berupa angka 1-3, lalu menyimpannya dalam variabel pilihan

    if pilihan == '1':
        print("data awal")
        print(data)
        # jika pengguna menginput angka 1 maka akan menampilkan seluruh isi variabel data (daftar barang) ke layar
    elif pilihan == '2':
        nama = input("Masukkan nama barang baru: ")
        kode = input("Masukkan kode barang: ")
        stok = input("Masukkan stok barang: ")
        harga = input("Masukkan harga barang: ")
        tambah_data(nama, kode, stok, harga)
        simpan_file()
        print("Berhasil menambah barang!")
        # jika pengguna menginput angka 2, pengguna di minta untuk memassukan detail barang baru berupa nama, kode, stok dan harga barang. 
        # memanggil fungsi tambah_data() untuk menambah data barang baru ke dalam daftar data
        # memanggil fungsi simpan_file() untuk menyimpan data barang baru ke dalam file barang.json
        # terakhir akan menampilkan teks "berhasil menambah barang!" di layar sebagai konfirmasi bahwa barang berhasil di tambahkan
    else:
        pilihan == '3'
        print("Keluar dari menu")
        break
        # jika pengguna menginput angka 3 maka akan menampilkan teks "keluar dari menu" dan akan keluar dari menu
        # break digunakan untuk menghentikan perulangan while True
