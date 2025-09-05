import statistics
import random

kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda x: x["satis"])

def yazar_satislari(kitaplar):
    sonuc = {}
    for k in kitaplar:
        sonuc[k["yazar"]] = sonuc.get(k["yazar"], 0) + k["satis"]
    return sonuc

turler = {k["tur"] for k in kitaplar}
bin_ustu = [k["isim"] for k in kitaplar if k["satis"] > 1000]

yeni_kitaplar = list(filter(lambda k: k["yil"] > 2020, kitaplar))
artirilmis_satislar = list(map(lambda k: k["satis"] * 1.1, kitaplar))
sirali_kitaplar = sorted(kitaplar, key=lambda k: k["satis"], reverse=True)

satislar = [k["satis"] for k in kitaplar]
ortalama = statistics.mean(satislar)
std_sapma = statistics.pstdev(satislar) 
tur_satislari = {}
for k in kitaplar:
    tur_satislari[k["tur"]] = tur_satislari.get(k["tur"], 0) + k["satis"]
en_cok_tur = max(tur_satislari, key=tur_satislari.get)


random.seed(42)  
train_size = int(len(kitaplar) * 0.7)
train_set = random.sample(kitaplar, train_size)
test_set = [k for k in kitaplar if k not in train_set]

train_ortalama = statistics.mean([k["satis"] for k in train_set])

test_ustunde = [k["isim"] for k in test_set if k["satis"] > train_ortalama]

print("En çok satan kitap:", en_cok_satan(kitaplar)["isim"])
print("Yazar satışları:", yazar_satislari(kitaplar))
print("Türler:", turler)
print("1000’den fazla satan kitaplar:", bin_ustu)
print("2020 sonrası kitaplar:", [k["isim"] for k in yeni_kitaplar])
print("Satış +%10:", artirilmis_satislar)
print("Satışa göre sıralı:", [k["isim"] for k in sirali_kitaplar])
print("Ortalama satış:", round(ortalama, 1))
print("En çok satış yapan tür:", en_cok_tur)
print("Standart sapma:", round(std_sapma, 1))
print("\nTrain set:", [k["isim"] for k in train_set])
print("Test set:", [k["isim"] for k in test_set])
print("Train ortalama satış:", round(train_ortalama, 1))
print("Test setinde ortalama üstü olanlar:", test_ustunde)
