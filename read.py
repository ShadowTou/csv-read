import pandas as pd
import csv
import os


pilihan_a = "1. Membaca csv menggunakan module pandas"
pilihan_b = "2. Membaca csv menggunakan module csv"

print("Selamat datang di aplikasi pembaca csv secara otomatis, silahkan lihat-lihat dulu!")
print(f"{pilihan_a}\n{pilihan_b}\n")


try:
    start = int(input("Jadi mau pilih mana?(1/2): ").strip())
except Exception as e:
    print(f"Ada error di sini: {e}")

if start not in [1,2]:
    print(f"Anda hanya bisa memilih antara 1 dan 2!")
    exit()


def csv_pandas(tujuan, file):
    if not os.path.exists(tujuan):
        print(f"Directory {tujuan} tidak ada!")
        return

    file_path = os.path.join(tujuan, file) 
    
    try:
       
        read = pd.read_csv(file_path)
        print(read)
    except Exception as e:
        print(f"Ada error di bagian ini {e}")

def csv_csv(tujuan, file):
    if not os.path.exists(tujuan):
        print(f"Directory {tujuan} tidak ada!")
        return

    file_path = os.path.join(tujuan,file)

    try:
        with open(file_path, "r", encoding="utf-8") as email:
            reader = csv.reader(email)

            for data in reader:
                print(", ".join(data))
    except Exception as e:
        print(f"Ada error di sini bang: {e}")




if(start == 1): 
   csv_pandas(r"D:\automationandscripting", "email.csv")
elif(start == 2):
    csv_csv(r"D:\automationandscripting", "email.csv")
else:
    print("Anda harus memilih antara angka 1 dan 2.")






