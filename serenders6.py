#operatörler

a = 5
print(a)
a += 6
print(a)  # a ya 6 eklenmiş hali ile yazar yani çıktı 11
a -= 3
print(a)
a *= 2
print(a)

print(2**3)   # 2 nin 3. kuvvetini alır, 2x2x2=8
b=3
b **= 2      # 3x3=9
print(b)

print(10/3)   #normal bölme işlemi
print(10//3)    # // ile yapılan bölme sonucunda küsüratı göstermez

print(98/10)     #çıktı 9.8
print(98//10)    #çıktı 9

#çoklu atama işlemi
c = d = 5
print(d)
e,f = 7,8
print(f)    #çıktı 8
print(e)     #çıktı 7

print(15%4)    # a mod b = kalanı çıktı olarak yazar,  3


#karşılaştırma operatörleri
print(a)
print(b)
# b*=8
print(a==b)
print(a!=b)


#FONKSİYONLAR
 #  3 çeşit fonksiyon var, basit, parametre alan ve değer döndüren fonskyion
def selamla():   # : sonraki komutların bu gruba ait olduğunu belirtir ,  def, fonksiyon tanımlarken kullanırız
    print("merhaba")
    print("iyi akşamlar")

selamla()    #ekrana merhaba ve iyi akşamlar yazar

def toplaa():
    print("Toplam:", 5+6)      #basit fonksiyon çünkü parametre istemiyor, sayıyı kendi tanımlıyor

toplaa()

def topla(aa,bb):   #parametre alan fonksiyon
    print("toplam:", aa+bb)

#topla()  #burada parametre olmadığı için hata verir çünkü yukarıda fonksiyonu parametreli olarak tanımladık
topla(5,6)
topla(3,5)
#topla(topla(1,2),4) #bu şekilde kullanmak için değer döndüren fonksiyon kullanmalıyız, bu şekilde çalışmaz


def toplam(aa,bb):
    return f"toplam: {aa+bb}"

print(toplam(4,8))    #print yazmadan topla fonksiyonu ekrana çıktı vermez çünkü yukarıda sadece return kullandık yani değer döndürdük

def carp(xx,yy):
    return xx*yy

print(carp(2,carp(2,4)))

#örnek
def tplm(a,b):
    return a+b

tplm(3,5)
print(tplm(7,4))
ee = tplm(2,4)
print(ee)

ff = tplm(7,tplm(3,6))
print(ff)

#def tplm(a,b=0):  #tplm fonksiyonu bir parametre ile de çalışabilir
#def tplm(a=0, b=0): #print(tplm()) şeklinde kullanım için
#def tplm(a=0,b):  #şeklinde kullanılamaz. default değerli parametreler diğerlerinden önce olamaz

#print(tplm())


# def hmmenu():
#     print("╔═════════════════════════════╗")
#     print("║    HESAP MAKİNESİ           ║") 
#     print("║                             ║")
#     print("║  1-Toplama                  ║")
#     print("║  2-Çıkarma                  ║")
#     print("║  3-                         ║")
#     print("║  4-                         ║")
#     print("║                             ║")
#     print("║  Seçiminiz nedir?           ║")
#     print("╚═════════════════════════════╝")
#     secim = input()

# def oyunlar():
#     print("bu menü henüz hazır değil")
#     secim = input()


# def anamenu():
#     print("╔═════════════════════════════╗")
#     print("║  VEKTOREL APP               ║") 
#     print("║                             ║")
#     print("║  1-Oyunlar                  ║")
#     print("║  2-Hesap M.                 ║")
#     print("║  3-                         ║")
#     print("║  4-Çıkış                    ║")
#     print("║                             ║")
#     print("║  Seçiminiz nedir?           ║")
#     print("╚═════════════════════════════╝")
#     secim = input()
#     if secim == "1" : oyunlar()
#     if secim == "2" : hmmenu()
#     if secim == "4" : exit()
#     else : anamenu()

# anamenu()


#FOR a giriş

# for a in range(5):
#     print(a,"Vektorel")    # 5 e kadar olan sayılarla beraber vektörel yazar, 0 Vektorel, 1 Vektorel... 5 e kadar yazar 5 dahil olmaz

# for b in range(5,10):
#     print(b)            # 5 ile 10 arası sayılarla yazar

for b in range(5,20,30):
    print(b)                   #  5 ile 20 arasındaki sayıları 3er fark ile yazar

#ÖRNEK
meyveler = ["Muz","Dut","Nar"]
for xx in meyveler:
    print(xx)

for aa in "Vektorel":
    print(aa)

import random
for h in range(5):
    print(random.randint(50,100))