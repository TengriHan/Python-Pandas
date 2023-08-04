import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\TengriHan\PycharmProjects\pythonProject3\vgsalesGlobale.csv")


#Veri setinin ilk 5 satırını getirir.
print(df.head())
print("----------------------------------")

#Veri tiplerini gösterir.
print(df.dtypes)
print("-----------------------------------")

#Kaç adet veri olduğunu hangi verilerin en fazla tekrar ettiğini gösterir
print(df.Genre.describe())
print("-------------------------------------")

#Genre değişkeninin içersindeki verilerin kaç adet olduğunu gösterir.
#Type komutu ile değişkenin hangi veri tipinde olduğunu anlayabiliriz.
#Yüzdelik olarak görmek istersek normalize = True komutu ile verilerin % kaç yer kapladığını görebiliriz.
print(df.Genre.value_counts())
print("---------------------------------------")

#Tekrar eden değerleri tek görmek için unique kullanılır.
print(df.Genre.unique())
print("----------------------------------------")
#Kaç değer olduğunu görmek istersek
print(df.Genre.nunique())
print("-----------------------------------------")

#Türlerin yıllara göre sayıları
print(pd.crosstab(df.Genre,df.Year))
print("------------------------------------------")

#Sayısal değişkenin ortalamasını, standart sapmasını ve hacmini gösterir
print(df.Global_Sales.describe())
print("-------------------------------------------")
#Sayısal değişkenin direkt ortalamasını almak için
print(df.Global_Sales.mean())
print("--------------------------------------------")

#Histogram grafiği ile gösterim
print(df.Year.plot(kind = "hist"))
plt.show()
print("----------------------------------------------")

#Bar grafiği ile gösterim
print(df.Genre.value_counts().plot(kind = "bar"))
plt.show()
print("-----------------------------------------------")
