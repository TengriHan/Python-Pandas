import pandas as pd
veri = {"isim" :["Furkan","Rabia","Tengri","Ülkü","Hakan","Adem","Barış"],
        "puan" :[50,85,55,90,95,45,60],
        "spor" :["Boks","Voleybol","Taekwondo","Yüzme","Futbol","Güreş","Hentbol"],
        "cinsiyet" :["E","K","E","K","E","E","E"]}
df = pd.DataFrame(veri)
print(df)
print("-----------------------------------------------")

#İlk 5 veriyi görmemizi sağlar
print(df.head())
print("------------------------------------------------")

#Son 5 veriiy görmemizi sağlar
print(df.tail())
print("-------------------------------------------------")

#İstersek sütun sıralamasını değiştirebilir veya yeni bir sütun ekleyebiliriz.
#İndexlere veri atayabiliriz.
df = pd.DataFrame(veri, columns=["isim","spor","cinsiyet","puan","yaş"],
                  index = ["bir","iki","üç","dört","beş","altı","yedi"])
print(df)
print("----------------------------------------------------")

#İstediğimiz sütunu bu şekilde çağırabiliriz.
print(df["spor"])
print("----------------------------------------------------")

#İstediğimiz belli bir satırı çağırırken
print(df.loc[["bir","iki"]])
print("-----------------------------------------------------")

#NaN olan bir değişkeni bu şekilde değiştirebiliriz.
df["yaş"] = 20
print(df)
print("------------------------------------------------------")

#Eğer herkes aynı yaşta değilse
deger = [70,18,20,30,35,22,20]
df["yaş"] = deger
print(df)
print("------------------------------------------------------")

#Bir koşul eklersek
df["geçti"] = df.puan >= 85
print(df)
print("-------------------------------------------------------")

#Bir sütun silmek istersek
del df["geçti"]
print(df)
print("--------------------------------------------------------")