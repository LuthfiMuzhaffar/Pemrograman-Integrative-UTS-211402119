import datetime
import calendar

def main():
    # masukkan jumlah hari
    jumlah_hari = int(input("Masukkan jumlah hari: "))

    tanggal_jumlah_hari = hitung_tanggal_jumlah_hari(jumlah_hari)

    nama_hari = dapatkan_nama_hari(tanggal_jumlah_hari)

    # Menampilkan tanggal jumlah hari dengan format 
    print(f"{nama_hari} on {tanggal_jumlah_hari.day} {dapatkan_nama_bulan(tanggal_jumlah_hari.month)} {tanggal_jumlah_hari.year}")

def hitung_tanggal_jumlah_hari(jumlah_hari):
    # melihat tanggal hari ini
    tanggal_hari_ini = datetime.date.today()
    # Menambahkan jumlah hari ke tanggal hari ini
    tanggal_jumlah_hari = tanggal_hari_ini + datetime.timedelta(days=jumlah_hari)
    return tanggal_jumlah_hari

def dapatkan_nama_hari(tanggal):
    # Menggunakan modul calendar untuk mendapatkan nama hari
    nama_hari = calendar.day_name[tanggal.weekday()]
    return nama_hari

def dapatkan_nama_bulan(bulan):
    # Menggunakan modul calendar untuk mendapatkan nama bulan
    nama_bulan = calendar.month_name[bulan]
    return nama_bulan

if __name__ == "__main__":
    main()
