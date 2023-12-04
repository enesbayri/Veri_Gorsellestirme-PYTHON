import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
"""
x=np.array(["a","b","c","d","e","f"])
y=np.random.randint(1,50,size=(6,1))

plt.plot(x,y,"green")
plt.xlabel("x degerleri")
plt.ylabel("y degerleri")
plt.title("X-Y grafiği")
plt.show()
----------------------------------------------------------------------

x=np.arange(1,10,2)
y=np.random.randint(1,10,5)

plt.plot(x,y,"red")
plt.xlabel("x degerleri")
plt.ylabel("y degerleri")
plt.title("X-Y GRAFİK")
plt.show()
-----------------------------------------------------------------------
x=np.arange(1,10,2)
y=np.random.randint(1,10,5)

plt.subplot(2,2,1)
plt.plot(x,y,"red")
plt.ylabel("Y1")

plt.subplot(2,2,4)
plt.plot(x,y,"blue")
plt.ylabel("Y2")

plt.subplot(2,2,3)
plt.plot(x,y,"green")
plt.ylabel("Y3")

plt.subplot(2,2,2)
plt.plot(x,y,"black")
plt.ylabel("Y4")
------------------------------------------------------------------------


x=np.arange(1,10,2)
y=np.random.randint(1,10,5)

fig=plt.figure(figsize=(6,6))
axes=fig.add_axes([0.1,0.1,0.3,0.3])
axes.plot(x,y,"black")


axes=fig.add_axes([0.45,0.1,0.5,0.5])
axes.plot(x,y,"red")

plt.show()
--------------------------------------------------------------------------
x=np.arange(1,10,2)
y=np.random.randint(1,10,5)

fig,axes=plt.subplots(nrows=4,ncols=1,figsize=(6,6))

axes[0].plot(x,y,color="red")
axes[0].set_title("Y1")

axes[1].plot(x,y,color="black")
axes[1].set_title("Y2")

axes[2].plot(x,y,color="green")
axes[2].set_title("Y3")

axes[3].plot(x,y,color="blue")
axes[3].set_title("Y4")


plt.tight_layout()


plt.show()
--------------------------------------------------------------------------------
x=np.arange(1,10,2)
y=np.random.randint(1,10,5)

fig,axes=plt.subplots(figsize=(6,6))

axes.plot(x,x**2,label="X^2",color="black",linewidth=3,linestyle=":",marker="v",markeredgecolor="red",markeredgewidth=3)
axes.plot(x,y,label="X-Y",color="blue",linewidth=3,linestyle="-",marker="o",markeredgecolor="red",markeredgewidth=3)

plt.legend()

plt.show()
--------------------------------------------------------------------------------

x=np.arange(1,10,2)
h=["a","b","c","d","e"]
y=np.random.randint(1,10,5)

#plt.pie(x,labels=h)
plt.plot(x,h,"red")
plt.plot(x,y,"blue")

plt.bar(x,h)
plt.scatter(x,h)
plt.hist(x)

datam={"enes":[80,100],"emre":[50,100]}
ders=["mat","fiz"]
#df=pd.DataFrame(datam,index=ders)
#df.plot(kind="area",stacked=False)
df=pd.DataFrame(datam,index=ders)
df.plot(kind="line",stacked=False)

plt.show()
"""
#**SEABORN**


df=sns.load_dataset('titanic')

#sns.barplot(x="class",y="fare",hue="who",data=df)
#print(df[(df["class"]=="First")&(df["who"]=="woman")]["fare"].mean())

#sns.countplot(data=df,x="class")
#print(df.groupby("class").count())

#sns.boxplot(x="class",y="fare",hue="who",data=df)
#print(df[(df["class"]=="First")&(df["who"]=="woman")]["fare"].describe())


#sns.swarmplot(x="who",y="fare",data=df)


#sns.jointplot(x="age",y="fare",data=df,kind="hex")
#sns.jointplot(x="age",y="fare",data=df,kind="scatter")
#sns.jointplot(x="age",y="fare",data=df,kind="kde")
#sns.jointplot(x="age",y="fare",data=df,kind="reg")
#sns.jointplot(x="age",y="fare",data=df,kind="hist")


#sns.pointplot(x="class",y="fare",hue="who",data=df)
#print(df[(df["class"]=="First")&(df["who"]=="woman")]["fare"].mean())


#sns.lmplot(x="age",y="fare",hue="class",col="who",col_wrap=1,data=df)


#sns.kdeplot(x="fare",hue="class",data=df)
#sns.kdeplot(x="fare",hue="class",multiple="stack",data=df)
#sns.kdeplot(x="fare",y="age",hue="who",data=df)



sns.violinplot(x="class",y="fare",hue="who",data=df)




plt.show()



