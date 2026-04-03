# Python OOP ve Pandas Veri Analizi Rehberi

> W3Schools Python & Pandas eğitim içerikleri temel alınarak hazırlanmış kapsamlı uygulama rehberi.  
> Kapsam: Nesne Yönelimli Programlama · CSV İşlemleri · Veri Temizleme · Gruplama · Raporlama

---

## İçindekiler

1. [Python Temelleri ve Nesne Yönelimli Programlama (OOP)](#1-python-temelleri-ve-nesne-yönelimli-programlama-oop)
2. [Pandas Kütüphanesine Giriş](#2-pandas-kütüphanesine-giriş)
3. [CSV Dosyaları ile Çalışma](#3-csv-dosyaları-ile-çalışma)
4. [Veri Temizleme (Cleaning Data)](#4-veri-temizleme-cleaning-data)
5. [Veri Analizi ve Gruplandırma](#5-veri-analizi-ve-gruplandırma)
6. [Raporlama ve Çıktı Alma](#6-raporlama-ve-çıktı-alma)

---

## 1. Python Temelleri ve Nesne Yönelimli Programlama (OOP)

Python, sade sözdizimi ve geniş kütüphane ekosistemi sayesinde hem web geliştirme hem de veri bilimi alanlarında tercih edilen popüler bir programlama dilidir. Nesne Yönelimli Programlama (OOP), kodu gerçek dünya kavramlarına benzeterek modüler, okunabilir ve yeniden kullanılabilir hale getirmeyi amaçlar.

### 1.1 Sınıf (Class) ve Nesne (Object)

Bir **sınıf**, belirli özelliklere ve davranışlara sahip nesnelerin üretileceği bir şablondur. **Nesne** ise bu şablondan türetilen somut bir örnektir.

```python
class Personel:
    """Şirketteki bir personeli temsil eden sınıf."""
    sirket = "Yalova Teknoloji A.Ş."   # Sınıf değişkeni (tüm nesneler paylaşır)

    def __init__(self, ad, departman, maas):
        # Nesne değişkenleri (her nesneye özgü)
        self.ad         = ad
        self.departman  = departman
        self.maas       = maas

    def bilgi_goster(self):
        return f"{self.ad} | {self.departman} | {self.maas:,.0f} ₺"

# Nesne oluşturma
p1 = Personel("Halil Arslan", "IT",      77_000)
p2 = Personel("Ayşe Kaya",   "Muhasebe", 52_000)

print(p1.bilgi_goster())   # Halil Arslan | IT | 77.000 ₺
print(p2.sirket)           # Yalova Teknoloji A.Ş.
```

> **Not:** `sirket` sınıf değişkeni tüm nesneler tarafından ortaklaşa kullanılır. `self.ad` gibi nesne değişkenleri ise her nesneye özeldir.

---

### 1.2 `__init__` Metodu

`__init__`, Python'da **yapıcı metot** olarak bilinir. Bir nesne oluşturulduğu anda otomatik çağrılır; nesnenin başlangıç durumunu (özelliklerini) tanımlamak için kullanılır.

```python
class BankaHesabi:
    def __init__(self, sahip, bakiye=0.0):
        self.sahip  = sahip
        self.bakiye = bakiye
        self._islem_sayisi = 0   # gizli değişken (kapsülleme)

    def para_yatir(self, miktar):
        if miktar <= 0:
            raise ValueError("Yatırılacak miktar pozitif olmalıdır.")
        self.bakiye += miktar
        self._islem_sayisi += 1
        print(f"{miktar:,.0f} ₺ yatırıldı. Yeni bakiye: {self.bakiye:,.0f} ₺")

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            raise ValueError("Yetersiz bakiye!")
        self.bakiye -= miktar
        self._islem_sayisi += 1
        print(f"{miktar:,.0f} ₺ çekildi. Yeni bakiye: {self.bakiye:,.0f} ₺")

hesap = BankaHesabi("Mehmet Demir", bakiye=10_000)
hesap.para_yatir(5_000)   # 5.000 ₺ yatırıldı. Yeni bakiye: 15.000 ₺
hesap.para_cek(3_000)     # 3.000 ₺ çekildi. Yeni bakiye: 12.000 ₺
```

---

### 1.3 `self` Parametresi

`self`, sınıf içindeki her metoda otomatik olarak geçirilen ve **o anki nesne örneğini** temsil eden özel bir parametredir. Python'da zorunlu olarak yazılmalıdır.

```python
class Dikdortgen:
    def __init__(self, en, boy):
        self.en  = en
        self.boy = boy

    def alan(self):
        return self.en * self.boy        # self sayesinde nesneye ait en ve boy kullanılır

    def cevre(self):
        return 2 * (self.en + self.boy)

    def __str__(self):                   # print() çağrıldığında gösterilecek metin
        return f"Dikdörtgen({self.en}x{self.boy})"

d = Dikdortgen(8, 5)
print(d)          # Dikdörtgen(8x5)
print(d.alan())   # 40
print(d.cevre())  # 26
```

---

### 1.4 Kalıtım (Inheritance)

Kalıtım, bir sınıfın (**alt sınıf**) başka bir sınıfın (**üst sınıf**) özellik ve metotlarını devralmasına olanak tanır. Kod tekrarını ortadan kaldırır ve hiyerarşik yapılar kurulmasını sağlar.

```python
# Üst sınıf (Parent)
class Calisan:
    def __init__(self, ad, maas):
        self.ad   = ad
        self.maas = maas

    def tanitim(self):
        return f"Çalışan: {self.ad}, Maaş: {self.maas:,.0f} ₺"

    def maas_hesapla(self, ay_sayisi):
        return self.maas * ay_sayisi


# Alt sınıf (Child) — Calisan'dan türüyor
class Yonetici(Calisan):
    def __init__(self, ad, maas, departman, prim_orani=0.15):
        super().__init__(ad, maas)        # Üst sınıfın __init__'ini çağır
        self.departman  = departman
        self.prim_orani = prim_orani

    def tanitim(self):                    # Metot geçersiz kılma (override)
        temel = super().tanitim()
        return f"{temel} | Departman: {self.departman} | Prim: %{self.prim_orani*100:.0f}"

    def prim_hesapla(self):
        return self.maas * self.prim_orani


class SaatlikCalisan(Calisan):
    def __init__(self, ad, saat_ucreti, calisilan_saat):
        toplam = saat_ucreti * calisilan_saat
        super().__init__(ad, maas=toplam)
        self.saat_ucreti    = saat_ucreti
        self.calisilan_saat = calisilan_saat

    def tanitim(self):
        return f"Saatlik Çalışan: {self.ad} | {self.calisilan_saat}s × {self.saat_ucreti}₺ = {self.maas:,.0f}₺"


# Kullanım
y  = Yonetici("Fatma Yıldız", 85_000, "IT", prim_orani=0.20)
sc = SaatlikCalisan("Ali Çelik", saat_ucreti=250, calisilan_saat=160)

print(y.tanitim())            # Çalışan: Fatma Yıldız, Maaş: 85.000 ₺ | Departman: IT | Prim: %20
print(f"Prim: {y.prim_hesapla():,.0f} ₺")  # Prim: 17.000 ₺
print(sc.tanitim())           # Saatlik Çalışan: Ali Çelik | 160s × 250₺ = 40.000₺
```

---

### 1.5 Kapsülleme (Encapsulation)

Kapsülleme, nesnenin iç verilerini dışarıdan doğrudan erişime kapatarak yalnızca tanımlı arayüzler üzerinden değiştirilebilmesini sağlar.

```python
class Urun:
    def __init__(self, ad, fiyat):
        self.ad      = ad
        self.__fiyat = fiyat    # __ ile başlayan değişken → özel (private)

    @property
    def fiyat(self):            # Getter
        return self.__fiyat

    @fiyat.setter
    def fiyat(self, yeni_fiyat):  # Setter — doğrulama eklenebilir
        if yeni_fiyat < 0:
            raise ValueError("Fiyat negatif olamaz!")
        self.__fiyat = yeni_fiyat

u = Urun("Laptop", 45_000)
print(u.fiyat)       # 45000
u.fiyat = 48_000     # setter çalışır
# u.__fiyat = -1     # AttributeError — doğrudan erişim engellenir
```

---

### 1.6 Polimorfizm (Polymorphism)

Farklı sınıfların aynı isimli metodu kendi bağlamına göre farklı biçimde uygulamasıdır.

```python
class Kare:
    def __init__(self, kenar): self.kenar = kenar
    def alan(self): return self.kenar ** 2
    def __str__(self): return f"Kare (kenar={self.kenar})"

class Daire:
    import math
    def __init__(self, yaricap): self.yaricap = yaricap
    def alan(self): return __import__('math').pi * self.yaricap ** 2
    def __str__(self): return f"Daire (yarıçap={self.yaricap})"

class Ucgen:
    def __init__(self, taban, yukseklik): self.taban = taban; self.yukseklik = yukseklik
    def alan(self): return 0.5 * self.taban * self.yukseklik
    def __str__(self): return f"Üçgen (taban={self.taban}, yükseklik={self.yukseklik})"

sekiller = [Kare(6), Daire(4), Ucgen(8, 5)]

for s in sekiller:
    print(f"{s} → Alan: {s.alan():.2f}")
# Kare (kenar=6) → Alan: 36.00
# Daire (yarıçap=4) → Alan: 50.27
# Üçgen (taban=8, yükseklik=5) → Alan: 20.00
```

---

## 2. Pandas Kütüphanesine Giriş

Pandas, NumPy üzerine inşa edilmiş, veri manipülasyonu ve analizi için tasarlanmış güçlü bir Python kütüphanesidir. Adı *Panel Data* teriminden gelir.

```python
import pandas as pd
import numpy as np
```

### 2.1 Series — Tek Boyutlu Veri Yapısı

```python
# Listeden Series oluşturma
maaslar = pd.Series([52_000, 65_000, 77_000, 48_000],
                    index=["Ayşe", "Mehmet", "Halil", "Zeynep"],
                    name="Maaş (₺)")

print(maaslar)
# Ayşe      52000
# Mehmet    65000
# Halil     77000
# Zeynep    48000
# Name: Maaş (₺), dtype: int64

print(f"Ortalama maaş : {maaslar.mean():,.0f} ₺")   # 60.500 ₺
print(f"En yüksek     : {maaslar.idxmax()} ({maaslar.max():,} ₺)")  # Halil
```

### 2.2 DataFrame — İki Boyutlu Tablo Yapısı

```python
data = {
    "Ad"             : ["Halil Arslan", "Ayşe Kaya", "Mehmet Demir", "Zeynep Çelik", "Ali Yıldız"],
    "Departman"      : ["IT", "Muhasebe", "IT", "İK", "Muhasebe"],
    "Maas"           : [77_000, 52_000, 68_000, 55_000, 49_000],
    "Performans"     : [4.8, 4.2, 3.9, 4.5, 4.0],
    "Egitim_Sayisi"  : [5, 3, 4, 6, 2],
}

df = pd.DataFrame(data)

print(df.shape)          # (5, 5) — 5 satır, 5 sütun
print(df.dtypes)         # her sütunun veri tipi
print(df.head(3))        # ilk 3 satır
print(df.describe())     # sayısal sütunların istatistikleri
print(df.info())         # bellek kullanımı ve null bilgisi
```

---

## 3. CSV Dosyaları ile Çalışma

### 3.1 Temel Okuma

```python
df = pd.read_csv("personel.csv")
print(df.head())
print(df.shape)
```

### 3.2 `read_csv` Parametreleri

| Parametre | Amaç | Örnek |
|-----------|------|-------|
| `sep` | Sütun ayırıcı karakter | `sep=';'` |
| `encoding` | Karakter kodlaması | `encoding='utf-8'` |
| `header` | Başlık satırı indeksi | `header=0` |
| `names` | Sütun adlarını manuel tanımlama | `names=['id','ad','maas']` |
| `usecols` | Yalnızca belirli sütunları yükleme | `usecols=['Ad','Maas']` |
| `dtype` | Sütun veri tipini zorla | `dtype={'Maas': 'int32'}` |
| `nrows` | Okunacak satır sayısı limiti | `nrows=1000` |
| `parse_dates` | Tarih sütunlarını datetime'a çevirme | `parse_dates=['baslangic_tarihi']` |
| `na_values` | Eksik değer olarak sayılacak ifadeler | `na_values=['-', 'N/A', '']` |
| `index_col` | Belirli sütunu indeks olarak kullanma | `index_col='id'` |

```python
# Kapsamlı örnek
df = pd.read_csv(
    "personel.csv",
    encoding     = "utf-8",
    sep          = ",",
    header       = 0,
    usecols      = ["Ad", "Departman", "Maas", "Performans", "baslangic_tarihi"],
    dtype        = {"Maas": "int32", "Performans": "float32"},
    parse_dates  = ["baslangic_tarihi"],
    na_values    = ["-", "N/A", "Bilinmiyor"],
    nrows        = 500,        # test için ilk 500 satır
)

print(df.dtypes)
# Ad                    object
# Departman             object
# Maas                   int32
# Performans           float32
# baslangic_tarihi  datetime64[ns]
```

### 3.3 Tarih Sütunlarından Bilgi Türetme

```python
df["baslangic_tarihi"] = pd.to_datetime(df["baslangic_tarihi"])

bugun = pd.Timestamp.today()
df["Kidem_Gun"]  = (bugun - df["baslangic_tarihi"]).dt.days
df["Kidem_Yil"]  = df["Kidem_Gun"] // 365
df["Baslangic_Ay"] = df["baslangic_tarihi"].dt.month_name(locale="tr_TR")

print(df[["Ad", "Kidem_Yil", "Baslangic_Ay"]].head())
```

---

## 4. Veri Temizleme (Cleaning Data)

Gerçek dünya verileri çoğunlukla eksik, hatalı veya tutarsız kayıtlar içerir. Kaliteli analiz için veriyi önce temizlemek gerekir.

### 4.1 Eksik Verileri Tespit Etme

```python
print(df.isnull().sum())          # her sütundaki null sayısı
print(df.isnull().sum() / len(df) * 100)  # yüzde olarak
```

### 4.2 Boş Hücreleri Temizleme (Empty Cells)

```python
# Yöntem 1 — Eksik satırları sil
df_temiz = df.dropna()                        # herhangi bir sütunda null varsa satırı sil
df_temiz = df.dropna(subset=["Maas"])         # sadece Maas sütununda null olanları sil

# Yöntem 2 — Doldurma (imputation)
df["Maas"]       = df["Maas"].fillna(df["Maas"].median())        # medyan ile doldur
df["Performans"] = df["Performans"].fillna(df["Performans"].mean())  # ortalama
df["Departman"]  = df["Departman"].fillna("Belirsiz")            # sabit değer

# Yöntem 3 — İleri/geri taşıma (zaman serilerinde kullanışlı)
df["Maas"] = df["Maas"].ffill()    # forward fill
df["Maas"] = df["Maas"].bfill()    # backward fill
```

### 4.3 Yanlış Format Düzeltme (Wrong Format)

```python
# Tarih dönüşümü — karma formatlı sütun
df["tarih"] = pd.to_datetime(df["tarih"], format="%d/%m/%Y", errors="coerce")

# Sayısal dönüşüm — para birimi sembolü içeren sütun
df["Maas"] = (
    df["Maas"]
    .astype(str)
    .str.replace("₺", "", regex=False)
    .str.replace(".", "", regex=False)
    .str.strip()
    .astype(float)
)

# Metin temizleme
df["Ad"] = df["Ad"].str.strip().str.title()    # baştaki/sondaki boşlukları kaldır, başharfleri büyüt
df["Departman"] = df["Departman"].str.upper()  # tümünü büyük harf yap
```

### 4.4 Hatalı Verileri Düzeltme (Wrong Data)

```python
# Mantıksız değerleri filtrele
df = df[df["Maas"] > 0]                    # negatif maaş olamaz
df = df[df["Performans"].between(0, 5)]   # puan 0–5 arasında olmalı

# Aykırı değerleri sınırla (IQR yöntemi)
Q1 = df["Maas"].quantile(0.25)
Q3 = df["Maas"].quantile(0.75)
IQR = Q3 - Q1
alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

df_temiz = df[(df["Maas"] >= alt_sinir) & (df["Maas"] <= ust_sinir)]
print(f"Aykırı değer sonrası: {len(df_temiz)} satır (öncesi: {len(df)})")

# Belirli değerleri değiştirme
df["Departman"] = df["Departman"].replace({
    "İT"    : "IT",
    "Bilgi İşlem": "IT",
    "Ik"    : "İK",
})
```

### 4.5 Mükerrer Kayıtları Kaldırma (Removing Duplicates)

```python
# Tespis
print(f"Toplam tekrar: {df.duplicated().sum()}")
print(df[df.duplicated(keep=False)])          # tekrarlayan tüm satırları göster

# Silme
df = df.drop_duplicates()                     # tüm sütunlara göre
df = df.drop_duplicates(subset=["Ad"])        # yalnızca Ad sütununa göre
df = df.drop_duplicates(subset=["Ad", "Departman"], keep="last")  # son kaydı tut
df = df.reset_index(drop=True)               # indeksi sıfırla
```

---

## 5. Veri Analizi ve Gruplandırma

### 5.1 Filtreleme

```python
# Tek koşul
df_yasli   = df[df["Yas"] > 25]

# Çoklu koşul
df_it_kıdem = df[(df["Departman"] == "IT") & (df["Kidem_Yil"] >= 3)]

# isin — birden fazla değere göre filtre
df_teknik  = df[df["Departman"].isin(["IT", "Mühendislik"])]

# str metodları
df_ali     = df[df["Ad"].str.startswith("Ali")]
df_arslan  = df[df["Ad"].str.contains("Arslan", case=False)]

# query — daha okunabilir sözdizimi
df_filtre  = df.query("Maas > 60_000 and Departman == 'IT'")
```

### 5.2 Gruplandırma — `groupby()`

```python
# Tek sütuna göre gruplama
gruplar = df.groupby("Departman")["Maas"]

print(gruplar.mean().round(0))     # departman bazında ortalama maaş
print(gruplar.max())               # en yüksek maaşlar
print(gruplar.count())             # her departmandaki personel sayısı
```

### 5.3 Named Aggregation — `agg()`

```python
departman_ozet = df.groupby("Departman").agg(
    ort_maas       = ("Maas",          "mean"),
    max_maas       = ("Maas",          "max"),
    min_maas       = ("Maas",          "min"),
    personel_sayisi = ("Ad",           "count"),
    ort_performans = ("Performans",    "mean"),
    toplam_egitim  = ("Egitim_Sayisi", "sum"),
).round(2).reset_index()

print(departman_ozet.to_string())
```

Örnek çıktı:

```
  Departman   ort_maas  max_maas  min_maas  personel_sayisi  ort_performans  toplam_egitim
0        IT    72500.0     77000     68000                2            4.35             9
1        İK    55000.0     55000     55000                1            4.50             6
2  Muhasebe    50500.0     52000     49000                2            4.10             5
```

### 5.4 Pivot Tablolar

```python
pivot = pd.pivot_table(
    df,
    values    = "Maas",
    index     = "Sehir",          # satır başlıkları
    columns   = "Departman",      # sütun başlıkları
    aggfunc   = "mean",           # ortalama maaş
    fill_value= 0,                # eşleşme yoksa 0 göster
    margins   = True,             # satır/sütun toplamları
    margins_name = "GENEL"
).round(0)

print(pivot)
```

```python
# Çoklu metrik pivot
coklu_pivot = pd.pivot_table(
    df,
    values  = ["Maas", "Performans"],
    index   = "Departman",
    aggfunc = {"Maas": ["mean", "max"], "Performans": "mean"},
    fill_value = 0,
).round(2)
```

### 5.5 Korelasyon Analizi

```python
korelasyon = df[["Maas", "Performans", "Egitim_Sayisi", "Kidem_Yil"]].corr()
print(korelasyon)

# Maas ile en güçlü ilişkili değişken
print(korelasyon["Maas"].drop("Maas").abs().idxmax())
```

### 5.6 Grafik (Plotting)

```python
import matplotlib.pyplot as plt

# Departman bazında ortalama maaş çubuk grafiği
departman_ozet.set_index("Departman")["ort_maas"].plot(
    kind  = "bar",
    color = "#2196F3",
    edgecolor = "black",
    title = "Departman Bazında Ortalama Maaş",
    ylabel = "Maaş (₺)",
    figsize = (8, 5)
)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("departman_maas.png", dpi=150)
plt.show()

# Performans dağılımı histogram
df["Performans"].plot(
    kind  = "hist",
    bins  = 10,
    color = "#4CAF50",
    edgecolor = "black",
    title = "Performans Puanı Dağılımı"
)
plt.xlabel("Performans")
plt.tight_layout()
plt.show()

# Maaş ile performans arasındaki ilişki (scatter)
df.plot(
    kind = "scatter",
    x    = "Maas",
    y    = "Performans",
    c    = "Kidem_Yil",
    colormap = "viridis",
    title = "Maaş — Performans İlişkisi",
    figsize = (8, 5)
)
plt.tight_layout()
plt.show()
```

---

## 6. Raporlama ve Çıktı Alma

### 6.1 CSV Çıktısı

```python
# Temel kayıt
df.to_csv("temiz_personel.csv", index=False, encoding="utf-8")

# Excel uyumlu (Türkçe karakter sorunu yaşamamak için)
df.to_csv("temiz_personel_excel.csv", index=False, encoding="utf-8-sig", sep=";")

# Seçili sütunları kaydetme
kolonlar = ["Ad", "Departman", "Maas"]
df[kolonlar].to_csv("ozet_rapor.csv", index=False, encoding="utf-8-sig")
```

### 6.2 Çok Sayfalı Excel Raporu — `pd.ExcelWriter`

```python
from datetime import date

dosya_adi = f"personel_raporu_{date.today():%Y%m%d}.xlsx"

with pd.ExcelWriter(dosya_adi, engine="openpyxl") as writer:

    # Sekme 1 — Ham Veriler
    df.to_excel(writer, sheet_name="Ham_Veriler", index=False)

    # Sekme 2 — Departman Özeti
    departman_ozet.to_excel(writer, sheet_name="Departman_Ozeti", index=False)

    # Sekme 3 — Pivot Tablo
    pivot.to_excel(writer, sheet_name="Sehir_Dept_Pivot")

    # Sekme 4 — Filtreli Veri (sadece IT departmanı)
    df[df["Departman"] == "IT"].to_excel(
        writer, sheet_name="IT_Personel", index=False
    )

print(f"Rapor oluşturuldu: {dosya_adi}")
```

> **`with` bloğunun önemi:** `ExcelWriter` nesnesi `with` ifadesiyle kullanıldığında, blok sona erdiğinde dosya otomatik olarak `writer.save()` ve `writer.close()` çağrısı yapılmaksızın güvenli biçimde kaydedilir ve kapatılır. `with` kullanılmaması durumunda dosyanın disk üzerinde tamamlanmaması riski doğar.

### 6.3 Excel Formatlamasi (openpyxl)

```python
from openpyxl.styles import PatternFill, Font, Alignment

with pd.ExcelWriter("formatli_rapor.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Personel", index=False)

    ws = writer.sheets["Personel"]

    # Başlık satırını renklendir
    baslik_rengi = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    for hucre in ws[1]:
        hucre.fill      = baslik_rengi
        hucre.font      = Font(color="FFFFFF", bold=True)
        hucre.alignment = Alignment(horizontal="center")

    # Sütun genişliklerini otomatik ayarla
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_len + 4
```

### 6.4 Tüm Adımları Birleştiren Tam İş Akışı

```python
import pandas as pd
from datetime import date

# --- 1. VERİ OKUMA ---
df = pd.read_csv(
    "personel.csv",
    encoding    = "utf-8",
    parse_dates = ["baslangic_tarihi"],
    dtype       = {"Maas": "int32"},
    na_values   = ["-", "N/A"],
)

# --- 2. VERİ TEMİZLEME ---
df = df.dropna(subset=["Ad", "Maas"])
df = df.drop_duplicates(subset=["Ad"])
df["Ad"]        = df["Ad"].str.strip().str.title()
df["Departman"] = df["Departman"].str.strip().str.upper()
df["Maas"]      = df["Maas"].clip(lower=0)

# --- 3. TÜRETME ---
bugun = pd.Timestamp.today()
df["Kidem_Yil"] = ((bugun - df["baslangic_tarihi"]).dt.days // 365).astype(int)

# --- 4. ANALİZ ---
departman_ozet = df.groupby("Departman").agg(
    Kisi_Sayisi    = ("Ad",         "count"),
    Ort_Maas       = ("Maas",       "mean"),
    Max_Maas       = ("Maas",       "max"),
    Ort_Performans = ("Performans", "mean"),
).round(2).reset_index()

pivot = pd.pivot_table(
    df,
    values    = "Maas",
    index     = "Departman",
    columns   = "Kidem_Yil",
    aggfunc   = "mean",
    fill_value= 0,
).round(0)

# --- 5. RAPORLAMA ---
with pd.ExcelWriter(f"rapor_{date.today():%Y%m%d}.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer,             sheet_name="Ham_Veriler",      index=False)
    departman_ozet.to_excel(writer, sheet_name="Dept_Ozet",        index=False)
    pivot.to_excel(writer,          sheet_name="Kidem_Maas_Pivot")

print("✅ Rapor başarıyla oluşturuldu.")
```

---

## Özet Tablosu

| Konu | Temel Araçlar | Ne İşe Yarar |
|------|---------------|--------------|
| OOP | `class`, `__init__`, `self`, `super()` | Kodu modüler ve yeniden kullanılabilir yapar |
| Kalıtım | `class Alt(Ust)` | Kod tekrarını ortadan kaldırır |
| Kapsülleme | `__`, `@property` | Veri bütünlüğünü korur |
| Polimorfizm | Method override | Genel arayüzler üzerinden farklı davranış |
| Veri Okuma | `pd.read_csv()` | CSV dosyalarını DataFrame'e yükler |
| Temizleme | `dropna()`, `fillna()`, `drop_duplicates()` | Analiz kalitesini artırır |
| Analiz | `groupby()`, `agg()`, `pivot_table()` | Özet istatistikler üretir |
| Raporlama | `to_csv()`, `pd.ExcelWriter` | Sonuçları kalıcı dosyalara yazar |

---

*Bu rehber Yalova Üniversitesi Çınarcık MYO — Veri Tabanı, Ağ Tasarımı ve Yönetimi Programı kapsamında hazırlanmıştır.*
