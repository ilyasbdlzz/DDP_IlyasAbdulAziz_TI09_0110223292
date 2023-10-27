
# soal kendaraan
car = ["SLC", "bluebird", "2.993 CC", "gray"]
car.append ("2,54 billion")
car.append ("4 wheel")
car.insert (2,"BMW, Sport Car")
print("1. The Car you choose is",car)
print("")
# Soal bangun datar
print('''2. Selamat Datang di Program penghitung Bangun datar, 
      
Silahkan pilih angka untuk memasukkan bangun datar yang akan dihitung. 
1. Persegi
2. Lingkaran
3. Segitiga''')
print("")
shape = input ("Masukkan angka/bangun datar : ")
match shape:
    case"persegi"|"Persegi"|"PERSEGI"|"1":
        sisi = input ("Masukkan sisi persegi : ")
        luas = int(sisi) * int(sisi)
        print("Luas persegi dengan sisi",sisi,"adalah", luas)
        
    case"lingkaran"|"Lingkaran"|"LINGKARAN"|"2":
        jari = float (input ("Masukkan jari-jari : "))
        pi = 3.14
        luaso = pi * jari * jari
        print("Luas lingkaran dengan jari-jari",jari,"adalah", luaso)
        
    case"segitiga"|"Segitiga"|"SEGITIGA"|"3":
        alass = float(input("Masukkan Alas segitiga : "))
        tinggis = float(input("Masukkan Tinggi segitiga : "))
        luass = int(alass) * int(tinggis)
        print("Maka luas segitiga dengan alas",alass,"dan tinggi",tinggis,"adalah",luass)
        
    case _:
        print("salah memilih cokk, Pilih antara 3 pilihan tadi!")
        