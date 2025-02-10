print("╔═════════════════════════════╗")
print("║  VEKTOREL APP               ║") 
print("║                             ║")
print("║  1-Toplama                  ║")
print("║  2-Çıkarma                  ║")
print("║  3-                         ║")
print("║  4-                         ║")
print("║                             ║")
print("║  Seçiminiz nedir?           ║")
print("╚═════════════════════════════╝")

print(5+3) #sayısaıl ifadeler tırnaksız yazılır
print(542)

#print(Vektorel) #Hata verir. string ifadeler tırnak işareti olmadan yazılmaz

a = 6       #değişken ifadedir
print(a)    #değişkenler tırnaksız

Vektorel = 78
print(Vektorel)


b  = 25
print(f"Seren {b} yasinda")   #sayısal değerleri string içinde kullanırken tırnak
                               #işareti öncesinde f yazılır ve sayısal değer
                              #süslü parantez içine alınır.

print("\nÖğrenci Bilgileri\n================")
print("Adı:\nSoyadı:\nNumarası:")     #\n new line, alt satıra geçer

print("\nAdı\t:\nSoyadı\t:\nNumarası:")  #\t tab, boşluk bırakır

no = 456
print("\nAdı\t:\nSoyadı\t:\nNumarası:",no)   #değişkenler tırnak işareti dışına
                                            #virgülle ayrılarak yazılır

ad = "Yusuf"
soyad = "Yılmaz"
print("\nAdı\t:",ad,"\nSoyadı\t:",soyad,"\nNumarası:",no)


abc = 5
efg = "Muhammed"
xx = len("Muhammed") #len fonksiyonu string uzunluğunu verir

print(abc)
print(efg)
print(xx)   #xx değişkeninde len fonksiyonu atanmış, kelime uzunluğunu verir
print(len("Seren"))  #çıktı: 5



c = 33
d = 22
a = str(c)   #sayısal ifadeyi stringe çevirir
b = str(d)
print(c+d)
print("33"+"22")   #çıktı:3322 (string olarak yzar) + ile yazıldığı için
                  #boşluk bırakmaz ama , ile yazsaydı boiluk bırakırdı
print(33+22)      #çıktı:55
print(a+b)        #değikenlerde sayısal değeri stringe çevirdiği için
                  #çıktı: 3322



ad = "Yağız"
soyad = "KARA"
no = 789

print("\nAdı:",ad,"\nSoyad:",soyad,"\nNumarası:",no)     #çıktı alttakilerle aynı
yazilacak = f"\nAdı:{ad}\nSoyadı:{soyad}\nNumarası:{no}"      
print(yazilacak)
print(f"\nAdı:{ad}\nSoyadı:{soyad}\nNumarası:{no}")

#PRİNT BİTTİ

#İNPUT GİRİŞ


ad = input()
soyad = input()
print(f"Ad {ad},Soyad {soyad}")



ad = input("Adınızı girin\t:")
soyad = input("Soyadınızı girin:")
print(f"Demek adın {ad},soyadın {soyad}.Güzel.")



