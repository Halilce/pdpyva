import pandas as pd

# 1) CSV dosyasını DataFrame olarak içeri al
df = pd.read_csv(
    'personel.csv',          # Çalışacağımız CSV dosyası
    encoding='utf-8',        # Türkçe karakter desteği
    parse_dates=['baslangic_tarihi']  # Tarih kolonunu datetime yap
)

rapor_departman = (
    df
    .groupby('departman')          # 1) Departmana göre gruplandır
    .agg(                          # 2) Her grup için özet hesaplar
        ort_maas = ('maas', 'mean'),
        ort_performans = ('performans_puani', 'mean'),
        ort_egitim = ('e_gitimi_sayisi', 'mean'),
        ort_uzaktan = ('uzaktan_calisma_gun', 'mean'),
        personel_sayisi = ('personel_id', 'count')
    )
    .reset_index()                 # 3) departman'ı normal kolon yap
)

rapor_sehir_departman = (
    df
    .groupby(['sehir', 'departman'])    # 1) İki kolonla grup
    .agg(
        ort_maas=('maas', 'mean'),
        ort_performans=('performans_puani', 'mean'),
        sayi=('personel_id', 'count')
    )
    .reset_index()
)

pivot_sehir_departman = pd.pivot_table(
    df,
    values='maas',          # Özetlenecek değer
    index='sehir',          # Satırlar
    columns='departman',    # Sütunlar
    aggfunc='mean',         # Özet fonksiyonu: ortalama maaş
    fill_value=0            # Eksik kombinasyonları 0 yap
)

# 1) Departman raporunu CSV olarak dışa aktar
rapor_departman.to_csv(
    'rapor_departman.csv',
    index=False,               # Satır index'ini yazma
    encoding='utf-8-sig'       # Excel'in düzgün okuması için
)

# 2) Birden fazla raporu tek Excel dosyasında farklı sayfalara yaz
with pd.ExcelWriter('personel_raporlar.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Ham_Veriler', index=False)
    rapor_departman.to_excel(writer, sheet_name='Departman', index=False)
    rapor_sehir_departman.to_excel(writer, sheet_name='Sehir_Dep', index=False)
    pivot_sehir_departman.to_excel(writer, sheet_name='Pivot_Maas', index=True)