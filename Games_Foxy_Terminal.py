import os
import platform
import random
Nama = input("Sebelum memulai permainan masukkan namamu terlebih dahulu: ")
def Clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
def Mainplay():
    huruf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    Mix_huruf = huruf.copy()
    random.shuffle(Mix_huruf)
    Jawaban = random.choice(Mix_huruf)
    Blueberry = 8
    print("<<<                    GAME DIMULAI                         >>>")
    print(Mix_huruf)
    Indeks = int(Mix_huruf.index(Jawaban[0]))+1
    Posisi = 100 / int(len(Mix_huruf)) * Indeks
    if Posisi > 80 :
        print(" Posisi : Fox tidak bergerak")
    elif Posisi > 60 :
        print(" Posisi : Fox bersuara ")
    elif Posisi > 40 :
        print(" Posisi : Fox menatapmu")
    elif Posisi > 20 :
        print(" Posisi : Fox bergerak")
    elif Posisi > 0 :
        print(" Posisi : Fox bersembunyi")
    while Blueberry > 0 :
        Tangkapfox = str(input("Hapus dan Hancurkan Semak[Satu Huruf Besar]: "))
        if Tangkapfox == Jawaban:
            Clear()
            print(f"{"="*7}==============================================={"="*7}")
            print(f"                                WIN                        ")
            print(f"         Selamat {Nama} kamu telah memenangkan permainan")
            print(f"            Aku akan memberimu 8 Blueberry Kembali    ")
            print(f"        Sisa Blueberry : {Blueberry-1} Semak Fox: {Jawaban} ")
            print(f"            Silahkan Menikmati Panen Blueberryku itu    ")
            print(f"{"="*7}==============================================={"="*7}")
            Next= input("Next Permainan [Y][N]: ")
            if Next != 0 :
                  Clear()
                  break
                  Homepage()
                  
        elif Blueberry == 1:
            Clear()
            print(f"{"="*7}==============================================={"="*7}")
            print(f"                                LOSE                       ")
            print(f"            Apakah benar sang {Nama} adalah si pencuri FOXY")
            print(f"                  Apakah kamu ingin bermain kembali?      ")
            print(f"                Bluberrymu Habis Fox bersembunyi di Semak {Jawaban}   ")
            print(f"                   Ingin Mencuri atau Mencari ?         ")
            print(f"{"="*7}==============================================={"="*7}")
            Next= input("Lanjutkan Permainan [Y][N]: ")
            if Next != 0 :
                Clear()
                Homepage()
                
            
        else:
            Clear()
            Blueberry -= 1
            print(f" === Fox masih belum tertangkap ===")
            print("")
            Mix_huruf.remove(Tangkapfox)
            print(f"Huruf semak tersisa: \n{Mix_huruf}")
            print("")
            Indeks = int(Mix_huruf.index(Jawaban[0]))+1
            Posisi = 100 / int(len(Mix_huruf)) * Indeks
            if Posisi > 80 :
                print(" Posisi : Semak berada dikanan")
                if 85 < Posisi <90 :
                    print(" Pergerakan : Fox berpindah semak !!!")
                elif 90 < Posisi <95 :
                    print(" Pergerakan :Fox berlari di semak-semak !!!")    
            elif Posisi > 60 :
                print(" Posisi : Semak berada diarea Tengah kanan")
                if 65 < Posisi < 70 :
                    print(" Pergerakan :Fox bersuara !!!")
                elif 70 < Posisi <75 :
                    print(" Pergerakan :Fox Bersembunyi !!!")    
            elif Posisi > 40 :
                print(" Posisi : Semak berada diTengah")
                if 45 < Posisi <50 :
                    print(" Pergerakan : Fox bergerombol !!!")
                elif 50 < Posisi <55 :
                    print(" Pergerakan : Fox berlarian !!!")    
            elif Posisi > 20 :
                print(" Posisi : Semak berada diarea Tengah kiri")
                if 25 < Posisi <30 :
                    print(" Pergerakan : Fox disekitarmu !!!")
                elif 30 < Posisi <35 :
                    print(" Pergerakan : Fox sudah menipumu !!!") 
            elif Posisi > 0 :
                print(" Posisi : Semak berada dikiri")
                if 5 < Posisi <10 :
                    print(" Pergerakan : Fox berpindah semak !!!")
                elif 10 < Posisi <15 :
                    print(" Pergerakan : Fox memberikan jejak !!!") 
            print("")
            print("Blueberrymu tersisa:", Blueberry)
            print("")
           
        
    
        
        

def Homepage():
    Clear()
    print("=========================================")
    print("")
    print(f"Hallo {Nama} Selamat Datang di Game FOXY")
    print("")
    print("@<  ~   @<  ~  @<  ~  @<  ~  @<  ~  @< ~ ")
    print("")
    print(f"       Apakah kamu suka Bluebery?       ")
    print("")
    print("=========================================")
    print("        Melanjutkan bermain [Y][N] :     ")
    print("")
    print("")
    Main= input("                   ")
    if Main == "Y" :
        Clear()
        def Play() :
             print(f"{"="*7}==============================================================={"="*7}")
             print(f"{"="*7}  Halo aku Petani Blueberry bantulah aku mencari Rubah Pencuri {"="*7}")
             print(f"{"="*7}        Bacalah Intruksi permainan Dikebunku ini!              {"="*7}")
             print(f"{"="*7}1.Cari Semak[?] dan Hancurkan semak dari Fox pencuri Blueberry {"="*7}")
             print(f"{"="*7}2.Gunakan 8 Bluberry untuk kesempatan memancing pergerakan Fox {"="*7}")
             print(f"{"="*7}3.Kesempatan itu juga digunakan untuk menghancurkan Sarang Fox {"="*7}")
             print(f"{"="*7}4.Jika Blueberrymu kamu habis, kamulah sang Foxy si Pencuri    {"="*7}")
             print(f"{"="*7}==============================================================={"="*7}")
             Play=input("Mulai Permainan [Y][N] :")
             if Play =="Y": 
                Clear()
                Mainplay()
             elif Play == "N":
                Clear()
                Homepage()
        Play()
    elif Main == "N":
        Clear()
        Homepage()
    else:
        Clear()
        print("    ~>=<~ Terjadi Kesalahan ~>=<~     ")
Homepage()