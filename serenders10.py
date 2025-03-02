#sınıf, obje

meyveler = ['elmalar','armut']
print(meyveler)
meyveler.append("Muz")    #dizinin sonuna ekler
print(meyveler)
meyveler.insert(1,"dut")  #dizinin 1. indeksine dut u ekler
print(meyveler)
meyveler.pop()   #dizinin son elemanını siler, parametreye indeks de verebiliriz özellikle silmek istersek
meyveler.append("Muz")
print(meyveler)
print(meyveler[2]) #dizinin 2. endeksini yazar dizinin son hali elmalar,dut,armut idi 2. endeks armut olur
print(meyveler[1:3])   #dizide 1. indeks dahil 3. indeks hariç aradki elemanları yazar
print(meyveler[:])  #dizideki tüm elemanları yazar
print(meyveler[:3]) # dizinin 3. endeksinden önceki elemanları yazar  3 dahildir
print(meyveler[2:]) #dizinin 2. endeksinden sonraki elemanları yazar 2 dahildir


#YEMEK MENÜ  2 boyutlu dizi

yemek_menusu = [
    ["tarhana","şehriye","mercimek"],
    ["musakka","mantı","karnıyarık"],                       # 2 boyutlu dizi: dizi içinde dizi
    ["tulumba","tiramisu","lokma"]
    ]

print(yemek_menusu)
print(yemek_menusu[2])   #dizide 2. indeksi yazar, tatlıları yazar
print(yemek_menusu[2][1])   #dizinin 2. indeksindeki dizinin 1. indeksini yani tiramisuyu yazar

print(["ee","rr","tt"][1])   # ee rr tt dizisindeki 1. indeksi yani rr yi yazar


#3 BOYUTLU DİZİ

yemek_menusu = {
    "corbalar":{"tarhana","şehriye","mercimek"},
    "yemekler":{"musakka","mantı","karnıyarık"},                       # 3 boyutlu dizi: dizi içinde dizi
    "tatlılar":{
        "tulumba":{"fiyat":100,"içindekiler":["un","su"]},
        "tiramisu":{},
        "lokma":{}}
}

print(yemek_menusu["tatlılar"])
print(yemek_menusu["tatlılar"]["tulumba"])
print(yemek_menusu["tatlılar"]["tulumba"]["fiyat"])
print(yemek_menusu["tatlılar"]["tulumba"]["içindekiler"])
print(yemek_menusu["tatlılar"]["tulumba"]["içindekiler"][0])      # dizi içinde dizi, 3 boyutlu


#class

class Ogrenci():           # oluşturduğumuz ogrenci sınıfı bir veri tipidir, 
                            #int,str gibi ogrenci de oluşturduğumuz bir veri tipidir. class ise bir veri modeli/veri kalıbıdır.
                            #sınıf adları Pascal case olur, tekil olur.
    ad = "--"
    no = 00
    def __init__(aa,x="",y=0):     # sınıfın fonksiyonu ile atama işlemi yapma, aa nesne, x ve y özelliktir (nesne özellikleri oluşturma)
        aa.ad = x                   # x="", y=0 yazma sebebimiz eğer bir değer atanmazsa x ve y için, x yani ad yerine boşluk bırakır, y yani no yerine 0 yazar ekrana
        aa.no = y    
        
        
ogrenci7 = Ogrenci("Osman",44)   # aa= ogrenci7 nesnesi,  x = ad , y = 44

     
ogrenci1 = Ogrenci     # class referansını öğrenci1 e atadı, bu kullanım yanlıştır
ogrenci2 = Ogrenci()     #ogrenci sınıfından yeni bir nesne oluşturdu
ogrenci3 = Ogrenci()       #ogrenci sınıfından yeni bir nesne oluşturdu
print(type(ogrenci1))
print(type(ogrenci2))

ogrenci1.ad = "Kemal"    #ogrenci1 sınıfın bir nesnesi değil, bu yüzden direk sınıfın değerini kemal yapar
print(ogrenci1.ad)
print(ogrenci2.ad)
print(ogrenci3.ad)       #ogrenci2 ve ogrenci3 de ekran kemal yazar çünkü ögrenci1 bir nesne değil  sınfın değerini aldı 59. satırda

ogrenci2.ad = "hasan"
print(ogrenci1.ad)
print(ogrenci2.ad)      #ekrana ogrenci2 hasan yazar ama diğerleri kemal yazar
print(ogrenci3.ad) 

ogrenci4 = Ogrenci()
ogrenci4.ad="Deniz"
ogrenci4.no=77

ogrenci5 = Ogrenci()     # '()'  paranteze init fonksiyonu denir yani oluşturma fonksiyonu
ogrenci5.ad="Yağız"
ogrenci5.no=88
  
print(ogrenci4.ad, ogrenci4.no)    #çıktı Deniz 77
print(ogrenci5.ad, ogrenci5.no)    #çıktı Yağız 88







