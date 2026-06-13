print("KAÇIŞ ODASINA HOŞ GELDİN")
print("bir odada kilitli kaldın...")
print("çıkmak için bulmacaları çözmelesin!\n")

puan=0

# 1. BULMACA
print
("1. BULMACA ")
cevap1=input("kapının şifresi nedir? (ipucu: 2+3*2=?):")


if cevap1=="8":
    print("doğru! kapı açıldı ama başka bir kapı var...\n")
    puan+=10
else:
    print(" yanlış! oda daha da karanlık oldu...\n")


#2.BULMACA
    print("2. BULMACA")
    cevap2= input("bir gün 24 saat ise 2 gün kaç saattir?:")

if cevap2== "48":
    print("doğru! gizli anahtar buldun...\n")
    puan+=10
else: 
    print("yanlış!  zaman kilidi aktif oldu...\n")


#3. BULMACA
    print("3. BULMACA")
    cevap3=input("şifreyi çöz: PY = 16, TH= 20 ise PT kaçtır?:")


if cevap3=="36":
        print("son kapı açıldı!\n")
        puan+=10
else:
    print("yanlış!son kapı kilitlendi...\n")

 #SONUÇ
print("oyuın bitti!")
print("puanın:",puan)


if puan ==30:
    print("MÜKEMMEL! odadan kaçtın! ")
elif puan>=20:
    print("İYİ!neredeyse kaçıyordun! ")


else:
        print(" BAŞARISIZ! tekrar dene...")
