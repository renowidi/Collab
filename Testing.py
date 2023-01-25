# print("Hello Reno")
# print("Hello Reno")

print("======Kalkulator Sederhana=======")

print("Pilih Operasi : ")
print("1. penjumlahan")
print("2. Pengurangan ")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat ")
print("6. Modulus")

a = int(input("pilih operasi (misal = 1) = "))

if a == 1:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    d = b+c
    print("Hasil penjumlahan =", d)


elif a == 2:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    d = b-c
    print("Hasil pengurangan = ",d)

elif a == 3:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))
    d = b*c
    print("Hasil Perkalian = ", d)

elif a == 4:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))
    d = b/c
    print("Hasil Pembagian = ", d)

elif a == 5:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))
    d = b**c
    print("Hasil kuadrat adalah = ", d)

elif a == 6:
    b = int(input("Masukkan angka pertama = "))
    c = int(input("Masukkan angka kedua = "))

    d = b%c
    print("Hasil Modulus = ", d)


