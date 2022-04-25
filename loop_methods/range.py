#--------------------------------------------------------------------------------
r = range(10);
sonuc = list(r);
print(sonuc);

#--------------------------------------------------------------------------------

rng = range(20, 100, 10); # 20 --> başlangıç değeri // 100 --> bitiş değeri // 10 -->artış miktarı
#başlangıç değeri dahildir, ancak bitiş değeri dahil değildir.

sonuc = list(rng);
print(sonuc);

#--------------------------------------------------------------------------------

#Sayı doğrusu oluşturunuz.
negatif = range(-10, 0, 1);
sonucNegatif = list(negatif);

pozitif = range(0, 11, 1);
sonucPozitif = list(pozitif);

print(sonucNegatif, sonucPozitif);

#--------------------------------------------------------------------------------

for i in range(100, 201):
    if(i % 10 == 0):
        print(i);