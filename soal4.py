class BMI:
    def __init__(self, berat_lb, tinggi_ft):
        self.berat = berat_lb  # berat badan
        self.tinggi = tinggi_ft * 0.3048  # tinggi badan

    def nilai_BMI(self):
        # Menghitung BMI 
        bmi = self.berat / (self.tinggi ** 2)
        return bmi

    def __eq__(self, lainnya):
        # Melakukan override 
        return self.berat == lainnya.berat and self.tinggi == lainnya.tinggi


if __name__ == "__main__":
    # Membuat dua objek BMI
    orang_1 = BMI(200, 6)  
    orang_2 = BMI(200, 6)

    # Menghitung dan mencetak nilai BMI untuk orang ke 1
    print("BMI untuk orang1:", orang_1.nilai_BMI())

    # Menghitung dan mencetak nilai BMI untuk orang ke 2
    print("BMI untuk orang1:", orang_2.nilai_BMI())

    # Membandingkan dua objek BMI
    print("Apakah orang ke 1 dan orang ke 2 sama?", orang_1 == orang_2)
