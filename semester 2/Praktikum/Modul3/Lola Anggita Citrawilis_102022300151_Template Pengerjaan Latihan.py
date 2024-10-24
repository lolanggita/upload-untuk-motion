import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('C:/Users/anggi/OneDrive/Documents/code/python/semester 2/Praktikum/Top 50 Football Player.csv')

# Menambahkan kolom rata-rata
df['Average'] = (df['Speed'] + df['Stamina'] + df['Attack'] + df['Defense']) / 4

# Mengurutkan data berdasarkan rata-rata tertinggi
sorted_value = df.sort_values('Average', ascending=False)

# Memfilter data berdasarkan umur antara 23 dan 28 tahun
df = df[(df['Umur'] >= 23) & (df['Umur'] <= 28)]

# Mengambil 11 data teratas
data_teratas = df.head(11)

# Menghitung total harga
Total_harga = data_teratas['Harga ($)'].sum()

# Mencari nilai tertinggi dari setiap kolom ability beserta nama pemain
speed_Tertinggi = data_teratas.loc[data_teratas['Speed'].idxmax(), 'Nama']
stamina_Tertinggi = data_teratas.loc[data_teratas['Stamina'].idxmax(), 'Nama']
attack_Tertinggi = data_teratas.loc[data_teratas['Attack'].idxmax(), 'Nama']
defense_Tertinggi = data_teratas.loc[data_teratas['Defense'].idxmax(), 'Nama']
speed = data_teratas['Speed'].max()
stamina = data_teratas['Stamina'].max()
attack = data_teratas['Attack'].max()
defense = data_teratas['Defense'].max()

# Menampilkan data
print(data_teratas)
print('\nTotal Harga: $',Total_harga)
print('\nSpeed Tertinggi :', speed_Tertinggi, speed)
print('Stamina Tertinggi :', stamina_Tertinggi, stamina)
print('Attack Tertinggi :', attack_Tertinggi, attack)
print('Defense Tertinggi :', defense_Tertinggi, defense)


