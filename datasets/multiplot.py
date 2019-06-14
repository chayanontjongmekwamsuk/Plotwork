import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")
df = df.copy()[df['type']=="organic"]
df['Date'] = pd.to_datetime(df["Date"])

df.sort_values(by="Date",ascending=True, inplace=True)

print(df.head())

graph_df = pd.DataFrame()
for region in df['region'].unique()[:16]:
    print(region)
    region_df = df.copy()[df['region']==region]
    region_df.sort_index(inplace=True)
    region_df.set_index("Date",inplace = True) 
    region_df[f'{region}_price25ma'] = region_df['AveragePrice'].rolling(25).mean()

    if graph_df.empty:
        #graph_df = region_df["price25ma"]       # region_df["price25ma"] means turn out the pandas series but we want the dataframe 
                                                    #so we use the region_df[["price25ma"]] be a dataframe
        graph_df = region_df[[f'{region}_price25ma']]      # we can add the spacific column like "averageprice"

    else:
        graph_df = graph_df.join(region_df[f'{region}_price25ma'])                 # bring the dataframe together

graph_df.plot(figsize=(8,5), legend=False)                                          # some value is NaN missing in the graph
graph_df.dropna().plot(figsize=(8,5), legend=False)                                 # drop out the NaN value
plt.show()