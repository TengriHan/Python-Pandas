import pandas as pd
import numpy as np

#Bir obje tanımlayalım ve indexlerini girelim
obje = pd.Series(np.arange(5),index=["a","b","c","d","e"])
print(obje )
print("-----------------------------------------------------")

print(obje["c"])
print("-----------------------------------------------------")

print(obje["a"])
print("-----------------------------------------------------")

#Eğer istediğimiz yerden itibaren sıralamak istersek
print(obje[0:3])
print("-----------------------------------------------------")


#Eğer belli indexleri almak istersek
print(obje[["a","c"]])
print("-----------------------------------------------------")

#Belli bir sayıdan küçük değerleri istersek
print(obje[obje<3])
print("-----------------------------------------------------")

#Yeni bir değer atama yapmak için
obje["b":"c"] = 5
print(obje)
print("-----------------------------------------------------")

#Dataframe için indexleme nasıl yapılır?
veri = pd.DataFrame(np.arange(16).reshape(4,4), index=["Kocaeli","Erzurum","Manisa","İstanbul"],
                    columns=["bir","iki","üç","dört"])
print(veri)
print("-----------------------------------------------------")

#Belli bir sütunu çağırmak istersek
print(veri["iki"])
print("-----------------------------------------------------")

#Birden fazla sütun için
print(veri[["bir","iki"]])
print("-----------------------------------------------------")

#Belli bir indexe kadar almak için
print(veri[:3])
print("-----------------------------------------------------")

#Mesela 4'ten büyük değerleri ekrana yazdıralım
print(veri[veri["dört"]>5] )

#5'ten küçük değerlere 0 değerini atayalım
veri[veri<5] = 0
print(veri)
print("-----------------------------------------------------")

#iloc için numaralar kullanılır
#loc için etiketler kullanılır
#Birinci indexe sahip satırın değerlerini görelim
print(veri.iloc[1])
print("-----------------------------------------------------")

#Birinci indexe sahip satırın 1.,2.,3. sahip satırlarını görelim
print(veri.iloc[1,[1,2,3]])
print("-----------------------------------------------------")

#Birden fazla index çağırarak istediğimiz satırları da görebiliriz.
print(veri.iloc[[0,2],[1,2,3]])
print("-----------------------------------------------------")


#Etiket kullanarak bunları nasıl çağırabiliriz.
print(veri.loc["Manisa",["bir","iki","üç"]])
print("-----------------------------------------------------")

print(veri.loc[:"İstanbul","dört"])
print("-----------------------------------------------------")
