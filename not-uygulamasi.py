
#Menu
    # 1- Not Gir
    # 2- Ortalamaları Göster
    # 3- Notları Kayıt Et
    # 4- Çıkış


def not_gir():
    ad = input("öğrenci adı: ")
    soyad = input("öğrenci soyadı: ")
    not1 = int(input("not 1: "))
    not2 = int(input("not 2: "))
    not3 = int(input("not 3: "))
    ortalama=(not1+not2+not3)/3
    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 80 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "BB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CB"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "CC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DC"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "DD"
    elif ortalama >= 40 and ortalama <= 49:
        harf = "FD"
    elif ortalama >= 0 and ortalama <= 39:
        harf = "FF"


    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ': ' + str(not1) + ',' + str(not2) + ',' + str(not3) + '\n')
        file.write(f"{ad} adlı öğrencinin ortalaması: {ortalama:.2f} ve harf notu: {harf}\n") 

def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for i in file:
            print(i)

def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for satir in file:
            liste.append(satir)

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            file2.writelines(liste)

        with open("yedek_dosya.txt", "w", encoding="utf-8") as file2:
            file2.writelines(liste)  
while True:
    islem = input("1- Not Gir\n2- Notları Göster\n3- Notları Kayıt Et\n4- Çıkış\nSeçim yapınız: ")

    if islem =="1":
        not_gir()
    elif islem=="2":
        notlari_oku()
    elif islem=="3":
        notlari_kaydet()
    elif islem == "4":
        print("Sistemden çıkış yapıyorsunuz...")
        break
    else:
        print("Geçersiz bir seçim yaptınız, lütfen tekrar deneyin.")