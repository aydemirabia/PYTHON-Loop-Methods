'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri
    ile buldurmaya çalışınız.
    ** random modülü kullanınız.
    ** 100 üzerinden puanlama yapıp, her soruyu 20 puan alınız.
    ** Hak bilgisi üzerinden kullanıcıdan alınız ve her soru 
       belirtilen can sayısı üzerinden hesaplansın.
'''

import random
sayi = random.randint(1, 100);
print(sayi);
can = int(input("Kac hakkiniz olsun istersiniz?: "))
hak = can;
sayac = 0;

while hak > 0:
    hak -=  1;
    sayac += 1;
    tahmin = int(input("Tahmin: "));
    
    if tahmin == sayi:
        print(f"Tebrikler  {sayac}. defada bildiniz. Toplam puanınız: {100 - ((100 / can) * sayac)}");
        break;
    elif tahmin >= sayi:
        print("Asagi");
    else:
        print("Yukari");
        
    if hak == 0:
        print(f"Hakkiniz bitti. Tutulan sayi {sayi} idi.");
        break;
