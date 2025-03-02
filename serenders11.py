#CLASS ÖRNEK

class Ilan():
    ilan_no = "---"
    ilan_adi = "---"
    ilan_aciklamasi = "Açıklama girilmedi"
    def __init__(self,a,b,c):
        self.ilan_no = a
        self.ilan_adi = b
        self.ilan_aciklamasi = c

    def ilan_bilgileri(self, uyelik_tipi):
        if uyelik_tipi == "premium": 
            print("merhaba çok değerli üyemiz")
            print(f"ilan adı:{self.ilan_adi},\n İlan no: {self.ilan_no}, \n İlan açıklaması: {self.ilan_aciklamasi}")

        if uyelik_tipi == "basic":
            print("merhaba değerli üyemiz")
            print(f"İlan adı:{self.ilan_adi}, \nİlan no:{self.ilan_no}, \n İlan açıkalaması: {self.ilan_aciklamasi}")


ilan_234 = Ilan("257","On numara şahin","Temiz, 210binde,..")
ilan_587 = Ilan("874","Kiralık ev","3+1 metroya yakın,kombili..")

ilan_234.ilan_bilgileri("premium")
ilan_234.ilan_bilgileri("basic")
ilan_587.ilan_bilgileri("premium")


# DOSYA İŞLEMLERİ 1-dosyaya veri yazma
#dosyalar verileri tutan yapılardır
#DOSYA OLUŞTURMAK İÇİN open fonksiyonu kullanılır
for a in range (10):
     open(f"rehber{a}.txt","w")   #zynpygtr klasöründe 10 tane rehber.txt dosyası oluşturur


#open("rehber.txt").write("Merhaba")  #dosya açma parametresi ("w") olmadığından okuma modunda açar
open("rehber1.txt","w").write("Merhaba") #"w" parametresi ile yazdığımız için yazma modu ile açar
open("rehber1.txt","w").write("Nasılsın") #rehber.txt dosyasında yeni bir bilgi yazdığımızda önceki kayboluyor
                                        # w modu öncekilerin silinmesine sebep olur

#dosya değişkeni oluşturarak aşağıda işimizi kolaylaştırdık
dosya = open("rehber1.txt","w")
dosya.write("Merhaba")
dosya.write("Nasılsın")      #bu haliyle hem merhabayı hem nasılsını yazar. çünkü w yi kullanmadık

#DOSYAYA VERİ EKLEME

def ekle():
    d = open("rehber.txt","a")   #append modunda açar (append ekleme modu demektir)
                                #önceden olmayan bir dosyayı da oluşturur

    print("╔═REHBERE EKLEME═════════════════════")
    print("║ Ad giriniz \t: ", end=""); ad = input()
    print("║ Numara giriniz \t: ", end=""); no = input()

    d.write(f"{ad} - {no}\n")
       

    #d.write("Merhaba\n")
    #d.write("Merhaba\n")   #rehber.txt dosyanına alt alta merhaba yazısını ekler w komutu gibi önceki yazıyı silmez

    d.close() #close kullanılmazsa dosya sorun çıkarabilir


def oku():
    d = open("rehber.txt","r") #açma modu parametresi olmazsa default olarak r (read) verir
    d = open("rehber.txt")    #yukarıdaki ile aynı işi yapar. okuma modu
    okunan = d.read()
    print(okunan)

oku()   # ekrana d dosyasına yazdırdığımız metinleri yazar