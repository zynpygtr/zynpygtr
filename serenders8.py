print("toplama yapan program")
a = 5
b = 3
c = a + b 
print("Sonuc:", c)

def toplama(a,b):
    return a + b

def carpma(a, b):
    return a * b

def cikarma(a, b):
    return a - b

def bolme(a, b):
    return a / b

def karekok(a):
    return a ** 0.5

print()
len("toplama yapan program")

# klavyeden komutları inceledik bu ders, yukarıdaki örnek onun için


#DATETİME
import time

print("merhaba")
time.sleep(2)   #time.sleep, yazılar arasında bekletir hepsi aynı anda ekrana yazmaz
print("naber")
time.sleep(2)

import datetime
print(datetime.datetime.now())   #tarihi ekrana yazdırır
print(datetime.datetime.now().year)   #yılı yazar
print(datetime.datetime.now().month)  #ayı yazar
print(datetime.datetime.now().hour)   #saati yazar

print(datetime.datetime.now().strftime("%d-%m-%Y %A"))  # şu anın örnek çıktı 19-02-2025 Wednesday
print(datetime.datetime.now().strftime("%H:%M"))   # şu anın sadece saat ve dakikayı yazdırır örnek çıktı 21:09