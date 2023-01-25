# print("Hello Reno & Rachmat")

print("======Kalkulator Sederhana=======")

print("Pilih Operasi : ")
print("1. penjumlahan")
print("2. Pengurangan ")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat ")
print("6. Modulus")

hitung = int(input("pilih operasi (misal = 1) = "))

# Penjumlahan
if hitung == 1:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    hasil = b+c
    print("Hasil penjumlahan =", hasil)

# Pengurangan
elif hitung == 2:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    hasil = b-c
    print("Hasil pengurangan = ", hasil)

# Perkalian
elif hitung == 3:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    hasil = b*c
    print("Hasil Perkalian = ", hasil)

# Pembagian
elif hitung == 4:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    hasil = b/c
    print("Hasil Pembagian = ", hasil)

# Pangkat
elif hitung == 5:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    hasil = b**c
    print("Hasil Pangkat adalah = ", hasil)

# Modulus
elif hitung == 6:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    hasil = b % c
    print("Hasil Modulus = ", hasil)
