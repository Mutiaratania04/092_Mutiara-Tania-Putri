# Program Menghitung Volume Balok

print("Program Menghitung Volume Balok")

p = int(input("Masukkan Panjang Balok : "))
l = int(input("Masukkan Lebar Balok : "))
t = int(input("Masukkan Tinggi Balok : "))

V = p * l * t
print("Rumus Menghitung Volume Balok V = p x l x t")
print("Hasil dari Hitung Volume Balok : ",V)


# Program Menghitung Volume Tabung

print("Program Menghitung Volume Tabung")

pi = 3.14
r = int(input("Masukan Jari-jari Tabung : "))
t = int(input("Masukan Tinggi Tabung : "))

V = pi * r ** 2 * t
print("Rumus Menghitung Volume Tabung V = pi x r**2 x t")
print("Hasil dari Hitung Volume Tabung : ",V)