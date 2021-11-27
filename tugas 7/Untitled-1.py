
def hapus_kontak(daftar_kontak):
    telp = input("No telp yang akan di hapus : ")
    
    index = -1
    
    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telp == kontak['telp']:
            index = i
            break

    if index == -1:
        print("Data kontak tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Berhasil menghapus data kontak")

def cari_kontak(daftar_kontak):
    nama_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_dicari.lower()) != -1:
            print("======================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telp : {kontak['telp']}")
            print("======================")


daftar_kontak = []
daftar_kontak.append({
    "nama" : "Budi",
    "email" : "budi@gmail.com",
    "telp" : "0909090909"
})

while True:
    print("Daftar Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Tutup Program")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        function.hapus_kontak(daftar_kontak)
    elif menu == "3":
        kontak = function.kontak_baru()
        daftar_kontak.append(kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("menu tidak tersedia")