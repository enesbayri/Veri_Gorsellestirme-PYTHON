import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("data.csv")
df=df.iloc[:,1:]


df["Value"]=df["Value"].str.replace("€","").str.replace("M"," 1000000").str.replace("K"," 1000")
df["Value"]=df["Value"].str.split(" ",expand=True)[0].astype("float")*df["Value"].str.split(" ",expand=True)[1].astype("float")
df["Value"]=df["Value"].fillna(0).astype("float")
#print(df["Value"].head(10))

fig,ax=plt.subplots(figsize=(12,6))
#ax=sns.countplot(x="Position",data=df)
#ax.set_xlabel("Position")

#ax=sns.kdeplot(x="Age",data=df)
#ax.set_xlabel("AGE")

#ax=sns.barplot(x="Preferred Foot",y="Value",data=df)

#ax=sns.pointplot(x="Position",y="Value",hue="Preferred Foot",data=df)

#ax=sns.stripplot(x="International Reputation",y="Potential",data=df)
#ax=sns.lmplot(x="International Reputation",y="Potential",data=df)

#ax=sns.barplot(x="International Reputation",y="Potential",hue="Preferred Foot",data=df)

#ax=sns.lineplot(x="Potential",y="Strength",data=df)
#ax=sns.pointplot(x="Potential",y="Strength",data=df)

#ax=sns.lineplot(x="Potential",y="Strength",hue="Preferred Foot",data=df)
#ax=sns.pointplot(x="Potential",y="Strength",hue="Preferred Foot",data=df)

plt.show()

