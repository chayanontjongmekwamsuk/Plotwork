import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("test1.csv")
print(data.iloc[1, :])
plt.plot(data.iloc[1, :])
plt.plot(data.iloc[2, :])
plt.plot(data.iloc[3, :])
plt.show()