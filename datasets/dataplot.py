import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")
#print(df)

'''
df.head()       #to find head of lists as much as the lists have
print(df.head(3))    # assume we want only 3 heads
print(df.tail(2))       #find 2 tails

print(df["AveragePrice"])
print(df["AveragePrice"].head())    #we can also use df.AveragePrice.head() but It can get u confuse
'''

#separate looking legend(topic)
albany_df = df[ df['region'] == "Albany"]
'''print(albany_df.head())'''

#print(albany_df.index)      # index is mean how the data in each column related to each other identification
'''
print(albany_df.set_index("Date"))  # still serching albany but sort by date
print(albany_df.head())
'''
albany_df = albany_df.set_index("Date")
### print(albany_df.head())


#plot graph
albany_df.plot()    # sort by date above stack
plt.show()
albany_df["AveragePrice"].plot()    #average price ploting
plt.show()