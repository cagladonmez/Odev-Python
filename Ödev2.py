#Odev 2
#Bir öğrenci kayit sistemi yazdiğimizi düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalim.

#Bu öğrenci kayit sistemine;

#Aldiği isim soy isim ile listeye öğrenci ekleyen
#Aldiği isim soy isim ile eşleşen değeri listeden kaldiran
#Listeye birden fazla öğrenci eklemeyi mümkün kilan
#Listedeki tüm öğrencileri tek tek ekrana yazdiran
#Öğrencinin listedeki index numarasi öğrenci numarasi olarak kabul edildiğini düşünerek öğrencinin numarasini öğrenmeyi mümkün kilan
#Listeden birden fazla öğrenci silmeyi mümkün kilan (döngü kullaniniz)
#fonksiyonlari geliştiriniz ve her bir fonksiyonu en az bir kere çağirarak konsolda test ediniz.

#Ödevde kullanacağiniz döngülerin bir tanesi for bir tanesi while döngüsü olmasi istenmektedir.
Ogrenciler = ["Çağla Dönmez","Damla Çözer","Sunay Sezer"]
 
def OgrenciEkle():
    Ogrenciler.append(input("Eklemek istediğiniz öğrencinin isim-soyismini giriniz:  "))
    print(Ogrenciler)

def OgrenciSil():
    OgrenciAdi = input("Silmek istediginiz öğrenci ismini yaziniz: ")
    Ogrenciler.remove(f"{OgrenciAdi}")
    print(Ogrenciler)

def OgrencileriYazdir():
    for i in range(len(Ogrenciler)):
        print(Ogrenciler[i])

def CokOgrenciEkle():
    while True:
     ogr = input("Eklemek istediğiniz öğrencinin isim-soyismini giriniz, eğer daha fazla eklemek istemiyorsaniz 'son' yaziniz:  ")
     if ogr =="son":break
     Ogrenciler.append(ogr)
    print(Ogrenciler)
     
def NumOgren():
   ogr = input("Numarasini öğrenmek istediğiniz öğrencinin ismini yaziniz: ")
   i=0
   while i<=len(Ogrenciler):
      if Ogrenciler[i]==ogr: 
         print(i)
         break
      i+=1

def CokOgrSil():
    for i in range(len(Ogrenciler)):
     OgrenciAdi = input("Silmek istediginiz öğrenci ismini yaziniz,eğer daha fazla silmek istemiyorsaniz 'son' yaziniz: ")
     if OgrenciAdi=="son": break
     Ogrenciler.remove(f"{OgrenciAdi}")
    print(Ogrenciler)
     
def menu():
 fonk=int(input("1-Ogrenci ekle\n2-Ogrenci sil\n3-Ogrencileri yazdir\n4-Birden fazla ogrenci ekle\n5-Ogrenci numarasini ögren\n6-Birden fazla ögrenci sil\nYapmak istediginiz islemin numarasini yaziniz: "))
 global secim
 if fonk>0 and fonk<=6:
    match fonk:
       case 1:
          secim=OgrenciEkle()
       case 2:
          secim=OgrenciSil()
       case 3: 
          secim=OgrencileriYazdir()
       case 4:
          secim=CokOgrenciEkle()
       case 5:
          secim=NumOgren()
       case 6:
          secim=CokOgrSil()
 else: 
   print("Hatali Değer Girdiniz\nLütfen yeni değer giriniz.")
   menu()
 return secim
menu()


