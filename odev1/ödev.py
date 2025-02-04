""" tarihString=input("enter a date")
print(tarihString) """
import os 
from datetime import datetime

tarih_string = input("enter a date:")
tarih_objesi = datetime.strptime(tarih_string, "%Y-%m-%d")

haftanin_gunu = tarih_objesi.strftime("%A")

bugun=datetime.now()
fark=(tarih_objesi-bugun).days

print(f"The date you entered: {tarih_objesi.strftime('%Y-%m-%d')}")
print(f"That day: {haftanin_gunu}")

if fark > 0:
    print(f"This day  {fark} day later")
elif fark < 0:
    print(f"This day {-fark} day before")
else:
    print("Bu tarih bugun")
    
dosya_adi = input("Enter a file name to save (e.g., result.txt): ") 

if os.path.exists(dosya_adi):
    secim = input("The file already exists. Do you want to overwrite it? (Y/N): ").strip().lower()
    if secim != 'y':  
        print("transaction cancelled")
        exit()

with open(dosya_adi, "w") as dosya:
    dosya.write(f"The daye you entered: {tarih_objesi.strftime('%Y-%m-%d')}\n")
    dosya.write(f"Day of the week: {haftanin_gunu}\n")
    
    if fark > 0:
        dosya.write(f"This date {fark} day later.\n")
    elif fark < 0:
        dosya.write(f"This date {-fark} day before.\n")
    else:
        dosya.write("This date is today!\n")

print(f"Results The results are saved in the {dosya_adi} file.")
