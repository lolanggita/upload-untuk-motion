import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:/Users/anggi/OneDrive/Documents/code/python/semester 2/16 Mei/SF_Air_Traffic_Passenger_Statistics.csv'
data = pd.read_csv(file_path)

# Soal 1
# Mendeteksi nilai hilang
missing_value = data.isnull().sum() / len(data) * 100
print("\nPresentase Nilai Hilang")
print(missing_value)

data_cleaned = data.fillna(method='ffill').fillna(method='bfill')   # Mengisi nilai hilang dengan metode yang sesuai

# Menampilkan persentase nilai hilang setelah pembersihan
missing_value_cleaned = data_cleaned.isnull().sum() / len(data) * 100
print("\nPersentase Nilai Hilang setelah Pembersihan")
print(missing_value_cleaned)

# Mendeteksi outlier menggunakan metode IQR
Q1 = data_cleaned['Passenger Count'].quantile(0.25)
Q3 = data_cleaned['Passenger Count'].quantile(0.75)
IQR = Q3 = Q1
outliers = data_cleaned[(data_cleaned['Passenger Count'] < (Q1 - 1.5 * IQR)) | (data_cleaned['Passenger Count'] > (Q3 + 1.5 * IQR))]

# Membuat plot boxplot untuk visualisasi outlier
plt.figure(figsize=(10, 6))
plt.boxplot(data_cleaned['Passenger Count'])
plt.title('Boxplot of Passenger Count')
plt.ylabel('Passenger Count')
plt.show()


# Soal 2
#
correlation_matrix = data_cleaned.corr()
print("\nMatriks Korelasi")
print(correlation_matrix)

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title('Correlation Heatmap')
plt.show()

data_cleaned['Activity Period'] = pd.to_datetime(data_cleaned['Activity Period'], format='%Y%m')
data_cleaned['Year'] = data_cleaned['Activity Period'].dt.year

plt.figure(figsize=(10,6))
sns.scatterplot(x='Year', y='Passenger Count', data=data_cleaned, scatter=False, color='red')
