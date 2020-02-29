import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data=pd.read_csv("hw_25000.csv")
boy=data.Height.values.reshape(-1,1)
kilo=data.Weight.values.reshape(-1,1)
#print(kilo)
regression=LinearRegression()
regression.fit(boy,kilo)
print(regression.predict([[62]]))
print(regression.predict([[65]]))

plt.scatter(data.Height,data.Weight)
x=np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red")
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Boy Kilo Verisi")
plt.show()

print(r2_score(kilo,regression.predict(boy)))


