# TUGAS 1
print ('''(Tugas 1.) 
    Print semua bilangan ganjil dari list berikut, hentikan perulangan ketika sudah melewati bilangan 553.''')
numbers = [
951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615,
83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  
386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
399, 162, 758, 219, 918,237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753,
470, 743, 527
]

for i in numbers:
    if i % 2 != 0 :
        print(i,end=", ")
    if i == 553:
        print(i,end=".")
        break

print("")
print("")

# TUGAS 2
print('''(Tugas 2.)
    Buat lah output dari menggunakan bahasa pemprograman python dengan : 
1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = ...''')
print("")
# untuk visualnya
p = 1
q = 2
r = []
while p < 20:
    print(p,end=" + ")
    p+=q 
    if p == 19:
        break
print(p,end=" = ")

# untuk penambahan jumlah setiap list
print()

nilai_list = []
counter = 1

while counter < 20: 
    nilai = counter
    nilai_list.append(nilai)  # Menambahkan nilai ke dalam list
    counter += 2  # Meningkatkan nilai counter
    
total = sum(nilai_list)
print("Nilai-nilai yang di-loop:", nilai_list)
print("Total nilai-nilai:", total)

print("")
# TUGAS 3

print('''(Tugas 3.)
    Buat program untuk minta input jumlah baris dan buat rangkaian berikut ini
*
**
***
****
Dan seterusnya sejumlah baris yang diinputkan
Gunakan for loop dengan range
''')
baris = int(input("Masukkan input baris = "))
for x in range (1,baris):
    print(x * "*")