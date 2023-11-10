import os
import platform
import math

def Clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
# print(f"{'='*7}    Selamat datang di Kalkulator Fisika Galvix     {'='*7}")
# print(f"{'='*7} Disini Galvix akan membantu Pekerjaan Fisika Kamu {'='*7}")

def menu_utama( ):
    print(f"{'='*7}    Selamat datang di Kalkulator Fisika Galvix     {'='*7}")
    print(f"{'='*7} Disini Galvix akan membantu Pekerjaan Fisika Kamu {'='*7}")
    print(f"{'='*7}       Perhitungan Matematika Dasar[1]         {'='*7}")
    print(f"{'='*7}          Perhitungan Jarak        [2]         {'='*7}")
    print(f"{'='*7}          Perhitungan Satuan Suhu  [3]         {'='*7}")
    print(f"{'='*7}         Perhitungan Trigonometri  [4]         {'='*7}")
    print(f"{'='*7}            Perhitungan Massa      [5]         {'='*7}")
    print(f"{'='*7}           Keluar dan Bersihkan    [0]         {'='*7}")
    


def Perjarak():
    print(f"{'='*7} Galvix sedang cari Pulau nih... {'='*7}")
    print(f"{'='*7}    Perhitungan satuan Jarak     {'='*7}")
    print(f"{'='*7}       Mm Milimeter  [1]         {'='*7}")
    print(f"{'='*7}       Cm Sentimeter [2]         {'='*7}")
    print(f"{'='*7}       Dm Desimeter  [3]         {'='*7}")
    print(f"{'='*7}       M  Meter      [4]         {'='*7}")
    print(f"{'='*7}       Dam Dekameter [5]         {'='*7}")
    print(f"{'='*7}       Hm HektoMeter [6]         {'='*7}")
    print(f"{'='*7}       Km Kilometer  [7]         {'='*7}")
    Satuan_jarak = {
        1: "Mm",
        2: "Cm",
        3: "Dm",
        4: "M",
        5: "Dam",
        6: "Hm",
        7: "Km"
    }
    Nilai = float(input("Masukkan nilai: "))
    Satuan_Awal = int(input("Masukkan satuan awal [1-7]: "))
    Satuan_Akhir = int(input("Masukkan satuan akhir [1-7]: "))

    if Satuan_Awal <= Satuan_Akhir:
        Pangkat = Satuan_Akhir - Satuan_Awal
        Hasil = Nilai / (10 ** Pangkat)
    else:
        Pangkat = Satuan_Awal - Satuan_Akhir
        Hasil = Nilai * (10 ** Pangkat)
    Clear()
    print(f"Hasil dari nilai awal {Nilai} {Satuan_jarak[Satuan_Awal]} menjadi {Satuan_jarak[Satuan_Akhir]} adalah {Hasil} {Satuan_jarak[Satuan_Akhir]}.")
    print(f"{'='*7}Galvix sudah menemukan island!{'='*7}")
    menu_utama()

def Permassa():
    print(f"{'='*7}Galvix sedang mencari Koin nih...{'='*7}")
    print(f"{'='*7}    Perhitungan satuan Massa     {'='*7}")
    print(f"{'='*7}       Mg Miligram   [1]         {'='*7}")
    print(f"{'='*7}       Cg Sentigram  [2]         {'='*7}")
    print(f"{'='*7}       Dg Desigram   [3]         {'='*7}")
    print(f"{'='*7}       G  Gram       [4]         {'='*7}")
    print(f"{'='*7}       Dag Dekamgram [5]         {'='*7}")
    print(f"{'='*7}       Hg Hektogram  [6]         {'='*7}")
    print(f"{'='*7}       Kg Kilogram   [7]         {'='*7}")
    Satuan_massa = {
        1: "Mg",
        2: "Cg",
        3: "Dg",
        4: "G",
        5: "Dag",
        6: "Hg",
        7: "Kg"
    }

    Nilai = float(input("Masukkan nilai: "))
    Satuan_Awal = int(input("Masukkan satuan awal [1-7]: "))
    Satuan_Akhir = int(input("Masukkan satuan akhir [1-7]: "))
    if Satuan_Awal <= Satuan_Akhir:
       Pangkat = Satuan_Akhir - Satuan_Awal
       Hasil = Nilai / (10 ** Pangkat)
    else:
       Pangkat = Satuan_Awal - Satuan_Akhir
       Hasil = Nilai * (10 ** Pangkat)
    Clear()
    print(f"Hasil dari nilai awal {Nilai} {Satuan_massa[Satuan_Awal]} menjadi {Satuan_massa[Satuan_Akhir]} adalah {Hasil} {Satuan_massa[Satuan_Akhir]}.")
    print(f"{'='*7} Galvix sudah menemukan koin!{'='*7}")
    

def kalkulator(bil1):
    operator = ["+", "-", "*", "/", "//", "**", "%", "="]
    hasil = bil1
    print("""
        Keterangan: 
        +   = Menjumlahkan kedua angka
        -   = Mengurangi kedua angka
        *   = Mengkalikan kedua angka 
        /   = Membagi kedua angka dengan hasil berupa bulat desimal
        //  = Membagi kedua angka dengan hasil berupa bilangan bulat
    **  = Memangkatkan angka 1 dengan angka 2 sebagai pangkatnya
    %   = Membagi angka 1 dengan angka 2 dan menampilkan hasil baginya
    =   = Mengakhiri operasi dan menampilkan hasil
     """)
    while True:
        operator1 = input("Masukkan operator yang diinginkan: ")
        if operator1 not in operator:
            print("Invalid Operator, Please try again")
            continue
        if operator1 == "=":
            return hasil
        bil2 = float(input("Masukkan angka yang akan dioperasikan: "))
        Clear()
        if operator1 == "+":
            hasil += bil2
            return hasil
        elif operator1 == "-":
            hasil -= bil2
            return hasil
        elif operator1 == "*":
            hasil *= bil2
            return hasil
        elif operator1 == "/" or operator1 == "//" or operator1 == "%":
            if bil2 == 0:
                print("Error, tidak bisa dibagi dengan nol")
                return hasil
            elif operator1 == "/":
                hasil /= bil2
                return hasil
            elif operator1 == "//":
                hasil //= bil2
                return hasil
            elif operator1 == "%":
                hasil %= bil2
                return hasil
        elif operator1 == "**":
            hasil **= bil2
            return hasil

def suhu():
    print(f"{'='*7}    Perhitungan Satuan Suhu     {'='*7}")
    print(f"{'='*7}       Celcius       (C)          {'='*7}")
    print(f"{'='*7}       Fahrenheit    (F)          {'='*7}")
    print(f"{'='*7}       Reamur        (R)          {'='*7}")
    print(f"{'='*7}       Kelvin        (K)          {'='*7}")
    print("Contoh = 100 C")
    while True:
        while True:
            inputan = input("Masukkan suhu yang akan dikonversi beserta satuannya:  ")
            data = inputan.split(" ")
            if len(data) != 2:
                print("Format input tidak valid. Contoh: 100 C")
            elif not data[0].isdigit():
                print("Angka dimasukkan tidak valid.")
            else:
                break
        konversi = input("Masukkan satuan yang diinginkan (C/F/R/K): ")
        suhu = float(data[0])
        satuan1 = data[1]
        if satuan1 == konversi:
            print("Hasil konversi adalah sama dengan satuan awal.")
        else: 
            if satuan1 == "C" or satuan1 == "c":
                if konversi == "F" or konversi == "f":
                    hasil = (suhu*9/5)  + 32
                    break    
                elif konversi == "R" or konversi == "r":
                    hasil = suhu*4/5 
                    break
                elif konversi == "K" or konversi == "k":   
                    hasil = suhu + 273
                    break
                else:
                    print("Satuan tidak valid, please try again.")
            elif satuan1 == "F" or satuan1 == "f":
                if konversi == "C" or konversi == "C":
                    hasil = (suhu*5/9) - 32
                    break    
                elif konversi == "R" or konversi == "r":
                    hasil = (suhu*4/9) - 32 
                    break
                elif konversi == "K" or konversi == "k":   
                    hasil = ((suhu*5/9)-32) + 273
                    break
                else:
                    print("Satuan tidak valid, please try again.")
            elif satuan1 == "R" or satuan1 == "r":
                if konversi == "F" or konversi == "f":
                    hasil = (suhu*9/4) + 32
                    break    
                elif konversi == "C" or konversi == "c":
                    hasil = suhu*4/5 
                    break
                elif konversi == "K" or konversi == "k":   
                    hasil = (suhu*4/5) + 273
                    break
                else:
                    print("Satuan tidak valid, please try again.")
            elif satuan1 == "K" or satuan1 == "k":
                if konversi == "F" or konversi == "f":
                    hasil = (9/5*(suhu-273)) + 32
                    break    
                elif konversi == "R" or konversi == "r":
                    hasil = 4/5*(suhu-273) 
                    break
                elif konversi == "C" or konversi == "c":   
                    hasil = suhu - 273
                    break
                else:
                    print("Satuan tidak valid, please try again.")
            else: 
                print("Satuan tidak valid, please try again.")
    print("Hasil dari konversi ", inputan, " adalah ", hasil, konversi)

def trigonometri():
    print(f"{'='*7} Galvix sedang mencarimu nih...  {'='*7}")
    print(f"{'='*7}   Pilih Fungsi Trigonometri     {'='*7}")
    print(f"{'='*7}       Sinus         [1]         {'='*7}")
    print(f"{'='*7}       Cosinus       [2]         {'='*7}")
    print(f"{'='*7}       Tan           [3]         {'='*7}")
    print(f"{'='*7}       Cosecan       [4]         {'='*7}")
    print(f"{'='*7}       Secan         [5]         {'='*7}")
    print(f"{'='*7}       Cotangen      [6]         {'='*7}")
    print(f"{'='*7}       Out           [0]         {'='*7}")
    fungsi=input("Pilih Fungsi[]:")
    h = 0
 
    if fungsi == "1":
        sudut=float(input("Masukkan Sudut:"))
        h = math.sin(sudut)
        print(f"Hasilnya adalah{h}")
    elif fungsi == "2":
        sudut=float(input("Masukkan Sudut:"))
        h= math.cos(sudut)
        print(f"Hasilnya adalah{h}")
    elif fungsi == "3":
        sudut=float(input("Masukkan Sudut:"))
        h = math.tan(sudut)
        print(f"Hasilnya adalah{h}")
    elif fungsi == "4":
        sudut=float(input("Masukkan Sudut:"))
        h = 1 / math.sin(sudut)
        print(f"Hasilnya adalah{h}")
    elif fungsi == "5":
        sudut=float(input("Masukkan Sudut:"))
        h = 1 / math.cos(sudut)
        print(f"Hasilnya adalah{h}")
    elif fungsi == "6":
        sudut=float(input("Masukkan Sudut:"))
        h = math.cos(sudut) / math.sin(sudut)
        print(f"Hasilnya adalah{h}")
    else:
        menu_utama()
        print("Fungsi trigonometri tidak valid")
        return
    

while True:
    menu_utama()
    perintah = input("Masukkan nomor perintah yang diinginkan: ")
    if perintah == "0":
        Clear()
        print(f"{'='*7}    Terimakasih telah menggunakan Kalkulator Fisika Galvix!:)     {'='*7}")
    
    elif perintah == "1":
        Clear()
        bil1 = float(input("Masukkan angka: "))
        hasil = kalkulator(bil1)
        print("Hasil: " + str(hasil))
    elif perintah == "2":
        Clear()
        Perjarak()
    elif perintah == "3":
        Clear()
        suhu()
    elif perintah == "4":
        Clear()
        trigonometri()
    elif perintah == "5":
        Clear()
        Permassa()
    else:
        Clear()
        print("Mohon maaf Datanya salah nih Kak, Isikan sesuai dengan Nomor yang ada yaahh")
        print("     Kami harap Kalian dapat mendukung dan menunggu proyek Galvix          ")
        print("                   Tetap Dukung kami para pengembang yaa!                  ")
