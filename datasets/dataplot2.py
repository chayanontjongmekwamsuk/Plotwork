import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")

'''     plot specifically keyword       '''

df['Date'] = pd.to_datetime(df["Date"])     #set the x-axis (date) properly
albany_df = df[df["region"]=="Albany"]      #set the dataframe from the csv file
albany_df.set_index("Date",inplace = True)  #set date to be a x-axis
# albany_df["AveragePrice"].plot()            #command to plot from the variable
# plt.show()                                  #command to show graph

        #############################################

'''         Spread the info         '''
# albany_df['AveragePrice'].rolling(25).mean().plot()       #.mean() is mean a column
# plt.show()

        #############################################

#print(albany_df.index)          #to find to sorting of information

        #############################################

'''     Method to index a smooth graph      '''

# print(albany_df.sort_index(inplace=True))
# albany_df['AveragePrice'].rolling(25).mean().plot()
#plt.show()

        #############################################

#albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()
# print(albany_df.head(3))                # the value will turn out a NaN because it has to rolling every 25 value
# print(albany_df.tail())                 
# print(albany_df.dropna().head(3))       # dropna means removing any row of NaN value

        #############################################

'''     romove warning      '''
albany_df = df.copy()[df["region"]=="Albany"]
albany_df.sort_index(inplace=True)
albany_df.set_index("Date",inplace = True) 
albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()

        #############################################

'''     plot all the region in one graph      '''

''' three method to list '''

print(df['region'].values.tolist())             #that will show all the list of region too much
print(set(df['region'].values.tolist()))        #list each value of showing region 
print(df['region'].unique())                    #easier way to list of region value

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

    #else:
        #graph_df = graph_df.join(region_df[f'{region}_price25ma'])                 # bring the dataframe together

# print(df['type'].unique())
# print(graph_df.tail())


                ############################################
'''     sorting values          '''
df.sort_values(by="Date",ascending=True,inplace=True)

print(df.head())

