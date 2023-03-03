#author:mcagabe19
#get helped from:w3schools

import time

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y

print("Lütfen bir işlem seçiniz.")

while True:
    secim = input("1:Toplama\n2:Çıkartma\n3:Çarpma\n4:Bölme\nSeçiminiz : ")

    if secim in ('1', '2', '3', '4'):
        try:
            s1 = float(input("İlk Sayı : "))
            s2 = float(input("İkinci Sayı : "))
        except ValueError:
            print("Lütfen Bir Sayı Giriniz.\n")
            continue

        if secim == '1':
            print(s1, "+", s2, "=", toplama(s1, s2))

        elif secim == '2':
            print(s1, "-", s2, "=", cikarma(s1, s2))

        elif secim == '3':
            print(s1, "x", s2, "=", carpma(s1, s2))

        elif secim == '4':
            try:
            	print(s1, "÷", s2, "=", bolme(s1, s2))
            	
            except ZeroDivisionError:
            	print("0 ile bölünmez.\n")
        
        yeni_islem = input("Başka işlem yapmak istermisiniz? (evet/hayir): ")
        if yeni_islem in ('evet', 'hayir'):
            try:
            	if yeni_islem == "evet":
            		continue

            	if yeni_islem == "hayir":
            		print('This Code Will Close After 3 Seconds...')
            		time.sleep(3)
            		break
            except ValueError:
                 print("Returning to true...")
                 continue
 
    else:
        print("Lütfen 1-4 arası sayı giriniz.")