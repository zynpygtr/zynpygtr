#VERİ ARAMA

import re
metin1 = "Bugün hava çok soğuk"
metin2 = "Bursa çok sıcak"
metin3 = "Bugün hava soğuk"
metin4 = "Çok güzel bir hava var"

aranan = "Çok"
#aranan= "^çok"   #dizide başta yazıyorsa çok kelimesini bulur
#aranan= "sıcak$"  #dizinin sonunda yazıyorsa sıcak kelimesini bulur
print(re.search(aranan,metin4))  #ekrana span=(0,3) yazar yani dizinin ilk 3 indeksinde yazdığını belirtir

dosya =  open  ("text.txt",encoding="utf8")
veri = dosya.read()
print(veri)
print(re.search("\d{10}", veri))
print("Bulunan telefon nu:", veri[568:578:])





