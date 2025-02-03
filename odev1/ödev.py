""" tarihString=input("enter a date")
print(tarihString) """
import os 
from datetime import datetime

tarih_string = input("enter a date:")
tarih_objesi = datetime.strptime(tarih_string, "%Y-%m-%d")

haftanin_gunu = tarih_objesi.strftime("%A")

bugun=datetime.now()
fark=(tarih_objesi-bugun).days

print(f"Girdiğiniz tarih: {tarih_objesi.strftime('%Y-%m-%d')}")
print(f"Bu gün: {haftanin_gunu}")

if fark > 0:
    print(f"Bu tarih {fark} gun sonra")
elif fark < 0:
    print(f"Bu tarih {-fark} gun onc")
else:
    print("Bu tarih bugun")
    
dosya_adi = input("Kaydetmek için dosya adini girin (orn: sonuc.txt): ") 

if os.path.exists(dosya_adi):
    secim = input("Dosya zaten var uzerine yazmak ister misiniz? (E/H): ").strip().lower()
    if secim != 'e':  
        print("islem iptal edildi")
        exit()

with open(dosya_adi, "w") as dosya:
    dosya.write(f"Girdiğiniz tarih: {tarih_objesi.strftime('%Y-%m-%d')}\n")
    dosya.write(f"Haftanın günü: {haftanin_gunu}\n")
    
    if fark > 0:
        dosya.write(f"Bu tarih {fark} gun sonra.\n")
    elif fark < 0:
        dosya.write(f"Bu tarih {-fark} gun once.\n")
    else:
        dosya.write("Bu tarih bugun!\n")

print(f"Sonuçlar {dosya_adi} dosyasına kaydedildi.")
