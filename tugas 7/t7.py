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