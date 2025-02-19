#range ile sayıları yazdırma
for a in range(30,50,3):
    print(a)

for xx in 'yiğit':
    print(xx*2,end="")   # çıktı yyiiğğiitt

ogrenciler = ["mustafa", "yağız","seren"]
for x in ogrenciler:
    print(x)

for x, e in enumerate(ogrenciler):       # enumerate fonksiyonuy dizideki stringleri 0 ile başlayarak numaralandırıyor 
    print(x, e)                          # çıktı: 0 mustafa    1 yağız     2 seren


abc = [i for i in range(10,20,3)]     # i yi kullandığımız zaman yazdığımız değerleri bir listeye atıyor
print(abc)                              #çıktı : [10, 13, 16, 19]


#FOR İLE ÇARPIM TABLOSU

for b in range(1,11):
    print("\n", b, "ler basamağı")
    print("______________")
    for c in range(1,11):
        print(b,"x",c)


#FOR İLE TURTLE 
import turtle

# for aa in range(4):
#     turtle.forward(100)
#     turtle.right(90)    #kare oluşturduk

# input()   #input koymamızın sebebi ekrana çizdirdiğimiz çizginin biz enter a basana kadar kaybolmasını istemiyoruz



# for cc in range(5):
#     turtle.forward(100)
#     turtle.right(72)     #beşgen oluşturduk

# input()

#RANDOM KÜTÜPHANESİ

import random as rnd  # as ile kütüphane isimlerini kısaltabiliriz

print(rnd.random())     # random kütüphanedir, random() fonksiyondur bu fonksiyonu kullandığımızda
                            #çıktı timer sayacından bir sayı yazdırıyor (0 ile 1 arasında)
print(rnd.randint(50,100))  #50-100 aralığından rastgele tam sayı verir (randint sayesinde tam sayı verir)


oyunSecenekleri = ["tas","kagıt","makas"]
print(rnd.choice(oyunSecenekleri)) 


import random
from turtle import *

speed(10)
renk = ["red","blue"]
for x in range(10):    # ekrana 10 kare yapmasını istiyoruz
    color(random.choice(renk))
    up()
    turtle.goto(random.randint(-200,200), random.randint(-200,200))   #goto komutu koordinatları belirler, ekranın rastgele bir koordinatında çıkması için yazdık
    down()    # up ve down fonksiyonlarını kareler arasında çizgi çizmesini istemediğimiz içn kullandık
    kenar = random.randint(30,100)    #kenar uzunlukları 30 ile 100 arasında rastgele olsun
    for ff in range(4):
        turtle.forward(kenar)
        turtle.right(90)
        