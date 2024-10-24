import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_excel('c:/Users/anggi/OneDrive/Documents/code/python/11mei/datacontoh11mei.xlsx')
print(data.head())
print(data.describe())

data.groupby('Jenis Kelamin').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()

data.groupby('Jurusan Sekolah SMA').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()


# Heatmap Jurusan Kuliah
plt.subplots(figsize=(8,8))
df_2dhist = pd.DataFrame({
    x_label: grp['Jurusan Kuliah'].value_counts()
    for x_label, grp in data.groupby('Jurusan Sekolah SMA')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('Jurusan Sekolah SMA')
plt.ylabel('Jurusan Kuliah')
plt.show()

# Histogram Umur 
a=plt.figure(figsize=(10,6))
sns.histplot(data['Umur'], kde=True)
# kde=kernel display
plt.title('Distribusi Umur')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')
a.show()
input("Tekan enter untuk melanjutkan ")

# Boxplot Hubungan Gaji dan Pengalaman Kerja
b=plt.figure(figsize=(10,6))
sns.scatterplot(x='Pengalaman Kerja (tahun)', y='Gaji', data=data)
plt.title('Hubungan Gaji dan Pengalaman Kerja')
plt.xlabel('Pengalaman Kerja (tahun)')
plt.ylabel('Gaji')
b.show()
input("Tekan enter untuk melanjutkan ")

# Boxplot Gaji berdasarkan Jurusan Kuliah
c=plt.figure(figsize=(12,8))
sns.boxplot(x='Jurusan Kuliah', y='Gaji', data=data)
plt.title('Distribusi Gaji berdasarkan Jurusan Kuliah')
plt.xlabel('Jurusan Kuliah')
plt.ylabel('Gaji')
plt.xticks(rotation=45)
c.show()
input("Tekan enter untuk melanjutkan ")

# Barplot Gaji berdasarkan Janis Kelamin
d=plt.figure(figsize=(10,6))
sns.barplot(x='Jenis Kelamin', y='Gaji', data=data)
plt.title('Rata - Rata Gaji Berdasarkan Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Gaji')
d.show()



# Membuat subset dari data yang hanya berisi kolom numerik
data_numerik = data.select_dtypes(include=['int64', 'float64'])
korelasi = data_numerik.corr()  # Membuat korelasi antar kolom numerik

# Visualisasi heatmap korelasi
e=plt.figure(figsize=(12,10))
sns.heatmap(korelasi, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap Korelasi Antar Fitur Numerik')
e.show()
input("Tekan enter untuk melanjutkan ")

# Membuat fungsi untuk memetakan kategori ke ID Unik
def map_categories(column):
    unique = column.unique()
    return {name: i for i, name in enumerate(unique)}

# Memetakan kategori ID
school_map = map_categories(data['Asal Sekolah'])
major_map = map_categories(data['Jurusan Sekolah SMA'])
job_map = map_categories(data['Pekerjaan'])

# Membuat sumber, target, dan nilai untuk Sankey diagram
source = []
target = []
value = []

for idx, row in data.iterrows():
    source.append(school_map[row['Asal Sekolah']])
    target.append(len(school_map) + major_map[row['Jurusan Sekolah SMA']])
    value.append(1)

    source.append(len(school_map) + major_map[row['Jurusan Sekolah SMA']])
    target.append(len(school_map) + len(major_map) + job_map[row['Pekerjaan']])
    value.append(1)

# Membuat label
labels = list(school_map.keys()) + list(major_map.keys()) + list(job_map.keys())

# Membuat Sankey Diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        label=labels
    ),
    link=dict(
        source=source, # indices correspond to labels
        target=target,
        value=value
    )
)])    
fig.update_layout(title_text="Sankey Diagram: Aliran Asal Sekolah, Jurusan, dan Pekerjaan", font_size=10)
fig.show()
input("Tekan enter untuk melanjutkan ")


# Histogram untuk distribusi umur 
fig = px.histogram(data, x='Umur', nbins=10, title='Distribusi Umur')
fig.update_layout(bargap=0.1)
fig.show()
input("Tekan enter untuk melanjutkan ")

# Boxplot untuk gaji menggunakan Plotly
fig = px.box(data, y='Gaji', title='Distribusi Gaji')
fig.show()
input("Tekan enter untuk melanjutkan ")

# Heatmap korelasi menggunakan Plotly
fig = px.imshow(korelasi, text_auto=True, aspect='auto',
                labels=dict(x='Fitur', y='Fitur', color='Korelasi'),
                title='Heatmap Korelasi Antar Fitur Numerik')
fig.show()
input("Tekan enter untuk melanjutkan ")