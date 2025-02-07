print(range(6))
print(*range(6))   # * işareti 0 ile 6 arasındaki her bir değeri yazar
                   # çıktı: 0 1 2 3 4 5

                   
print(*range(6,9))   # 6 ile 9 arasındaki sayıları yazar, çıktı: 6 7 8

print(*range(60,100,5))  # 60 ile 100 arasındaki sayıları 5 er farkla yazar
                        # çıktı: 60 65 70 75 80 85 90 95

print(*range(60,100,5),sep="-")    # sep:separate(aralık)
                                   # çıktı: 60-65-70-75-80-85-90-95
                                   
print(*range(60,100,5),sep="\n")     #yukarıdaki seriyi alt alta yazar


print("muz","dut","nar",sep="--")       # çıktı: muz--dut--nar


print("Adınızı giriniz:")
print("Soyadınızı giriniz:")        #pyhton da gizli bir end parametresi var
                                     #bu sebeple print içinde yazanları alt alta yazar

print("Adınızı giriniz:",end="\t")        #end parametresinde \t yazdığımız için
print("Soyadınızı giriniz:",end="#Bitti") # alt satıra geçmeden boşluk bırakır
                                # çıktı: Adınızı giriniz:   Soyadınızı giriniz:#Bitti



#f, format vw %s

ad = "Erdiinç Dönmez"
not1 = 80
not2 = 90
print("Ad:",ad,", 1.Not:",not1)

print(f"Ad: {ad}, 1.Not: {not1}")# f = format  %s =(string)
                                 #bu ikisi string biçimlendirme için kullanılır
print("ortalama: {}" .format((not1+not2)/2))
print("100'den kalan %s" %(100-(not1+not2)/2))


print("deneme")
#diyaz ya da hashtag işareti sonrasında, bulunduğu yerden itibaren
#satır sonuna kadar açıklama ifadesi olarak kabul edilir.

"""
Açıklama ifadeleri ( comments) üç tek tırnak veya üç çift tırnak arasına
çok satırlı olacak şekilde kullanılabilir.
"""


# pyhton' da tek bir satırda tek bir komut yazılır
# ya da iki komut arasına ; koyulur    örnek:
print("merhaba")  ; print("nasılsın")


input()
input()     # enter a basılana kadar girilenleri bir string içine atar
            # bu şekilde çalıştırırsak çöpe atar

not1 = 49
print(not1*2)

not1 = input ()   # girileni not1 isimli kutuya attı

print(not1*2) # * işlemi stringleri tekrar ettirir.örnk: 30 girersek çıktı:3030


#girilen stringi sayıya çevirmek için 1. yöntem
not1 = input("1. sınav nedir?")

print(int(not1)*2)  #int fonksiyonu stringi tam fonksiyona dönüştürür.

#girilen stringi sayıya çevirmek için 2. yöntem
not2 = int(input("2. sınav nedir?"))
print(not2*2)

vize1 = int(input("vize notun:"))
final1 = int(input("final notun:"))
print(f"1. sınavın {vize1} , 2. sınavın {final1} ise \nOrtalaman:\
{(vize1+final1)/2}")


#örnekler

ad = input("Adın ne?")        #ekrana giren isimle Merhaba ... yzar
print(f"Merhaba {ad}") 

kenar = int(input("karenin kenarı kaç cm?"))    #karenin çevresini hesaplar
print(f"karenin çevresi: {kenar*4}cm")

knr = int(input("karenin kenarı kaç cm?"))      #karenin alanını hesaplar
print(f"bu karenin alanı: {knr*knr}cm")


s1 = int(input("1. sayıyı giriniz:"))       #girilen 2 sayıyı toplar
s2 = int(input("2. sayıyı giriniz:"))
print(f"Toplam: {s1+s2}")

yas = int(input("doğum yılınızı giriniz:"))
print(f"yaşınız: {2025-yas}")
