""" tarihString=input("enter a date")
print(tarihString) """
from datetime import datetime

tarih_string = input("enter a date:")
tarih_objesi = datetime.strptime(tarih_string, "%Y-%m-%d")

print(tarih_objesi)

