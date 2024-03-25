import datetime

def main():
    # Memasukkan bilangan bulat 
    bil_bulat = int(input("Masukkan bilangan bulat: "))

    # Menghitung jumlah hari dalam tahun ini
    hari_tahun = hitung_jumlah_hari_di_tahun()

    # Memastikan tidak membagi dengan nol
    if hari_tahun != 0:
        # Melakukan pembagian
        hasil = bil_bulat / hari_tahun
        # Menampilkan hasil dengan sebelas desimal
        print("Hasil bagi:", format(hasil, ".11f"))


def hitung_jumlah_hari_di_tahun():
    # Mengecek tanggal hari ini
    hari_ini = datetime.date.today()
    # Menghitung jumlah hari dalam tahun ini
    tanggal_awal_tahun = datetime.date(hari_ini.year, 1, 1)
    tanggal_akhir_tahun = datetime.date(hari_ini.year, 12, 31)
    jumlah_hari = (tanggal_akhir_tahun - tanggal_awal_tahun).days + 1
    return jumlah_hari

if __name__ == "__main__":
    main()
