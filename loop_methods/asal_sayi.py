# Girilen bir sayının asal sayı olup olmadığını kontrol ediniz.

sayi = int(input("Sayi: "));
asalMi = True;

if sayi == 1:
    asalMi = False;

for i in range(2, sayi):
    if(sayi % i == 0):
        asalMi = False;
        break;

if asalMi:
    print("Sayi asal sayidir.");
else:
    print("Sayi asal degildir.");