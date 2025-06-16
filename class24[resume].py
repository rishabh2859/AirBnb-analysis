#python3 "/Users/mac/class2/class24[resume].py"
#installing dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#loading data
data=pd.read_csv('/Users/mac/Downloads/datasets.csv')
# data exploration
print(data.head())
print(data.tail())
print(data.info())
print(data.shape)
print(data.describe())
# data cleaning
print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())
print(data.duplicated().sum())
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())
print(data.dtypes)
data['id']=data['id'].astype(object)
data['host_id']=data['host_id'].astype(object)
df=data[data['price']<1500]
print(data.dtypes)
sns.histplot(data=df,x='price',bins=100)
plt.title('Price Distribuition')
plt.ylabel("Frequency")
sns.boxplot(data=df,x='price')
sns.histplot(data=df,x='availability_365')
plt.show()
print(df.groupby(by='neighbourhood_group')['price'].mean())
df['price_per_bed']=df['price']/df['beds']
print(df.groupby(by='neighbourhood_group')['price_per_bed'].mean())
sns.barplot(data=df,x='neighbourhood_group',y='price',hue='room_type')
sns.scatterplot(data=df,x='number_of_reviews',y='price',hue='neighbourhood_group')
sns.pairplot(data=df,vars=['price','minimum_nights','number_of_reviews','availability_365'],hue='room_type')
sns.scatterplot(data=df,x='latitude',y='longitude',hue='room_type')
corr=df[['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'beds']].corr()
sns.heatmap(data=corr,annot=True)
plt.show()