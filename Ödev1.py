#    1-     VERİ TİPLERİ
#  Pythonda 5 standart veri türü var.
#  Sayılar: sayısal değerleri saklayan veri tipi.
#  Katar(string): Karakterleri saklar. Bunlar harfler sayılar ve noktalama işaretleri olabilir.
#  Liste: Çoğu dilde bulunan dizilere benziyor. Köşeli parantez içerisinde virgüllerle ayrılmış veriler yazılarak kullanılıyor. Ancak dizilerde tek veri türü
# toplayabiliyorduk. Listeye birden fazla veri türü yazabiliyoruz. Bu yönüyle bize esneklik sağlıyor.
#  Tuple: Tuple listelere benziyor ancak köşeli parantez yerine normal parantez ile yazılıyor. Bir diğer farkı ise sadece read-only modda olması.
#  Dictionary: Bir çeşit hash tablo türü. Anahtar-değer çiftlerinden oluşur. Bir sözlük anahtarı neredeyse her python tipi olabilir. Ancak çoğunlukla sayılar ya da
# dizilerdir. Değerler ise herhangi bir python nesnesi olabilir. Küme parantezleri ile çevrelenir ve değerler köşeli parantezler kullanılarak atanabilir ve erişilebilir.
#     2-
# Kodlama io Careers kısmındaki istenen form verileri değişken olarak tutulmaktadır. Örneğin e-posta adresimiz string türünde saklanırken iş arayıp aramadığımızı soran
# kısım boolean türünde tutulmaktadır.
#    3-
# Siteye giriş yaparken girdiğimiz şifre ve e-posta kısmında if else yapıları kullanılır.
eposta = input("E-posta adresinizi giriniz: ")
sifre = input("Sifrenizi giriniz: ")
if (eposta == "odev@gmail.com") and (sifre =="odev123") : print("E-posta ve sifreniz dogru.")
else : print("Yanlis e-posta veya sifre girdiniz.")