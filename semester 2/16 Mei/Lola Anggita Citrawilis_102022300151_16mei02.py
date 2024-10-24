import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'C:/Users/anggi/OneDrive/Documents/code/python/semester 2/16 Mei/Melbourne_housing_FULL.csv'
data = pd.read_csv(file_path)
print(data.head(5)) # Menampilkan 5 baris pertama

# Menghitung jumlah baris dan kolom 
data_column_len = len(data.columns)
data_rows_len = len(data)
print("column =", data_column_len)
print("rows =", data_rows_len)

# Menampilkan tipe data 
data_type = data.dtypes
print("\ntipe data :")
print(data_type)

# Menampilkan jumlah nilai yang hilang
missing_value = data.isnull().sum()
print("\nJumlah Nilai Hilang :")
print(missing_value)

# Menampilkan deskripsi statistik
# mean_price = data['Price'].mean()
# median_price = data['Price'].median()
# max_price = data['Price'].max()
# min_price = data['Price'].min()
# print("\nDeskripsi statistik 'Price' ")
# print("Mean :", mean_price)
# print("Median :", median_price)
# print("Max :", max_price)
# print("Min :", min_price)

# mean_Landsize = data['Landsize'].mean()
# median_Landsize = data['Landsize'].median()
# max_Landsize = data['Landsize'].max()
# min_Landsize = data['Landsize'].min()
# print("\nDeskripsi statistik 'Landsize' ")
# print("Mean :", mean_Landsize)
# print("Median :", median_Landsize)
# print("Max :", max_Landsize)
# print("Min :", min_Landsize)

# mean_BuildingArea = data['BuildingArea'].mean()
# median_BuildingArea = data['BuildingArea'].median()
# max_BuildingArea = data['BuildingArea'].max()
# min_BuildingArea = data['BuildingArea'].min()
# print("\nDeskripsi statistik 'BuildingArea' ")
# print("Mean :", mean_BuildingArea)
# print("Median :", median_BuildingArea)
# print("Max :", max_BuildingArea)
# print("Min :", min_BuildingArea)

statistik = data[['Price', 'Landsize', 'BuildingArea']].describe()
print(statistik)