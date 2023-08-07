#Bu projemizde pandas sorularını çözüyoruz.
#Zorluk : kolay

#Pandası yüklemeyi ve pd ismi ile çağırma
import pandas as pd
#Numpy kütüphanesini yüklüyoruz
import numpy as np
from pandas import DataFrame

#Pandasın versiyonunu kontrol etme
print(pd.__version__)
print("----------------------------------------------")

#Pandasın kullandığı tüm kütüphanelerin sürümleri
print(pd.show_versions())
print("----------------------------------------------")


#DataFrame'in temelleri DataFrame'lerde veri seçme, sıralama, ekleme ve toplamaya yönelik temel rutinlerden birkaçını yapalım

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#Bu sözlük verilerinden dizin etiketlerine sahip bir DataFrame df oluşturun.
df: DataFrame = pd.DataFrame(data, index=labels)
print(df)
print("-----------------------------------------------")

#Veri tiplerinin özelliklerini görelim
print(df.info())
print("------------------------------------------------")

#İlk 3 satırı döndürelim
print(df.head(3))
print("------------------------------------------------")

#Sadece hayvan ve yaş sütunlarını çağıralım
print(df[["animal","age"]])
print("-------------------------------------------------")

#Hayvan ve yaş sütunlarındaki 3,4,8 verileri görelim
print(df.loc[df.index[[3,4,8]],['animal', 'age']])
print("--------------------------------------------------")

#Ziyaretçi sayısı 3'ten fazla olanları çağıralım
print(df[df["visits"]>3])
print("---------------------------------------------------")

#Yaşın eskik olduğu sütunları çağıralım
print(df[df['age'].isnull()])
print("---------------------------------------------------")

#Hayvanın kedi olduğunu ve yaşının 3'ten küçük olduğu satırları çağıralım
print(df[(df["animal"] == "cat") & (df["age"] < 3)])
print("----------------------------------------------------")

#Yaşı 2 ve 4(dahil) olanları çağıralım
print(df[df["age"].between(2,4)])
print("----------------------------------------------------")

#f satırındaki yaşı 1.5 olarak değiştirelim
df.loc["f","age"] = 1.5

#Ziyaretçilerin toplamını hesaplayalım
print(df["visits"].sum())
print("------------------------------------------------------")

#Her farklı hayvan için ortalama yaşı hesaplayalım
print(df.groupby("animal")["age"].mean())
print("-------------------------------------------------------")

#Her hayvan türünün sayısını sayalım
print(df["animal"].value_counts())
print("--------------------------------------------------------")

#Yaştaki değerlere göre azalan ardından ziyaretler sütunundaki değere göre artan düzende sıralayın(i satırı ilk d satırı sonda olacaktır.)
print(df.sort_values(by=['age', 'visits'], ascending=[False,True]))
print("---------------------------------------------------------")

#priority sütunu "evet" ve "hayır" içeriyor. Bu sütunu boolean değerleriyle yer değiştirelim
df['priority'] = df['priority'].map({'yes': True, 'no': False})
print(df["priority"])
print("----------------------------------------------------------")

#Hayvan sütunundaki yılan isimlerini piton olarak değiştirelim
df["animal"] = df["animal"].replace("snake","python")
print(df["animal"])
print("------------------------------------------------------------")
