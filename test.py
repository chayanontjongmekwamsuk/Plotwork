import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("test1.csv")
print(data.iloc[1, :])

for i in range(1, 12, 1):   #range( start, stop, step)
    print(i)
    plt.plot(data.iloc[i, :])

# plt.plot(data.iloc[1, :])
# plt.plot(data.iloc[2, :])
# plt.plot(data.iloc[3, :])
# plt.plot(data.iloc[4, :])
# plt.plot(data.iloc[5, :])
# plt.plot(data.iloc[6, :])
# plt.plot(data.iloc[7, :])
# plt.plot(data.iloc[8, :])
# plt.plot(data.iloc[9, :])
# plt.plot(data.iloc[10, :])
# plt.plot(data.iloc[11, :])

plt.show()