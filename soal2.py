# tulis program python yang membaca angka (tanggal pengujian hari ini) dan mencetak produk dari semua nilai dari 1 hingga angka itu
def main():
    # masukkan tanggal ujian hari ini
    tanggal = int(input("Masukkan tanggal ujian hari ini: "))

    # Menghitung produk dari semua nilai dari 1 hingga angka tersebut
    product = hitung_product(tanggal)

    # Menampilkan hasil product
    print("Produk dari semua nilai dari 1 hingga", tanggal, "adalah:", product)

def hitung_product(angka):
    produk = 1
    for i in range(1, angka + 1):
        produk *= i
    return produk

if __name__ == "__main__":
    main()
