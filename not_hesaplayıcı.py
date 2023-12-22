from os import system

while True:
    print("VİZE FİNAL NOT ORTALAMA HESAPLAMA PROGRAMINA HOŞ GELDİNİZ producer by Efi Avni")
    str(input("DEVAM ETMEK İÇİN ENTERA BASIN"))
    vize = int(input("Vize notunuzu girin: "))
    final = int(input("Final notunuzu girin: "))
    ortalama = vize*40/100+final*60/100
    print(ortalama)

    if (ortalama >= 85):
        print(f"Not ortalamanız: {ortalama} Harf notunuz A")
    elif (ortalama >= 70) and (ortalama < 85):
        print(f"Not ortalamanız: {ortalama} Harf notunuz B")
    elif (ortalama >= 60) and (ortalama < 70):
        print(f"Not ortalamanız: {ortalama} Harf notunuz C")
    elif (ortalama >= 40) and (ortalama < 60):
        print(f"Not ortalamanız: {ortalama} Harf notunuz D")
    elif (ortalama >= 0) and (ortalama < 40):
        print(f"Not ortalamanız: {ortalama} Harf notunuz F")
    else:
        print("")

    if (ortalama >= 0) and (ortalama < 40):
        print("KALDINIZ!!")
    else:
        print("GEÇTİNİZ!!")
    
    devam = input("Yeniden hesaplamak için 'Y' tuşuna, çıkmak için 'Q' tuşuna basın: ")
    if devam.upper() == 'Q':
        break
    system("cls")


        
        