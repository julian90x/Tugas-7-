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