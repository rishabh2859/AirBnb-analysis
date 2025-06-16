
# Airbnb Data Analysis using Python

This project analyzes Airbnb listings data using Python for data cleaning, exploration, and visualization. The analysis provides insights into pricing, availability, and location-based trends.

## 📁 Dataset

- The dataset is assumed to be a CSV file located at: `/Users/mac/Downloads/datasets.csv`.

## 📦 Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

## 📊 Steps Performed

### 1. **Data Loading**

```python
data = pd.read_csv('/Users/mac/Downloads/datasets.csv')
```

### 2. **Exploratory Data Analysis (EDA)**

```python
print(data.head())
print(data.tail())
print(data.info())
print(data.shape)
print(data.describe())
```

### 3. **Data Cleaning**

- Check and drop nulls
- Check and remove duplicates
- Convert data types of `id` and `host_id` to object

```python
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)
data['id'] = data['id'].astype(object)
data['host_id'] = data['host_id'].astype(object)
```

### 4. **Filtering**

- Filtered listings with `price < 1500` for cleaner visualization

```python
df = data[data['price'] < 1500]
```

### 5. **Visualizations**

- **Price Distribution**

```python
sns.histplot(data=df, x='price', bins=100)
plt.title('Price Distribution')
plt.ylabel("Frequency")
```

- **Boxplot of Price**

```python
sns.boxplot(data=df, x='price')
```

- **Availability**

```python
sns.histplot(data=df, x='availability_365')
```

- **Average Price by Neighbourhood Group**

```python
df.groupby(by='neighbourhood_group')['price'].mean()
```

- **Price Per Bed**

```python
df['price_per_bed'] = df['price'] / df['beds']
df.groupby(by='neighbourhood_group')['price_per_bed'].mean()
```

- **Barplot: Price vs Room Type by Neighbourhood**

```python
sns.barplot(data=df, x='neighbourhood_group', y='price', hue='room_type')
```

- **Scatterplot: Reviews vs Price**

```python
sns.scatterplot(data=df, x='number_of_reviews', y='price', hue='neighbourhood_group')
```

- **Pairplot of Key Numerical Features**

```python
sns.pairplot(data=df, vars=['price','minimum_nights','number_of_reviews','availability_365'], hue='room_type')
```

- **Geolocation Visualization**

```python
sns.scatterplot(data=df, x='latitude', y='longitude', hue='room_type')
```

- **Correlation Heatmap**

```python
corr = df[['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'availability_365', 'beds']].corr()
sns.heatmap(data=corr, annot=True)
```

## ✅ Conclusion

This analysis helps in understanding:
- Distribution and variation in prices
- Price per bed across neighborhoods
- Room availability and popularity
- Location-wise trends and hotspots

The visual insights are helpful for hosts, customers, and analysts to make data-driven decisions in Airbnb ecosystem.
