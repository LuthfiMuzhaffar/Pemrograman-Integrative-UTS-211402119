def main():
    with open("input.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    total_jumlah = sum(numbers)

    # Format jumlahnya dengan pemisah koma dan tiga digit
    format_jumlah = "{:,.3f}".format(total_jumlah)

    print("hasil penjumlahan:", format_jumlah)

if __name__ == "__main__":
   main()
