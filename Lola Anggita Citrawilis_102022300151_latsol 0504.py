import numpy as np
nilai_Eren = {
    'Agama' : 70,
    'Seni budaya': 84,
    'Bahasa inggris':80,
    'Matematika': 88,
    'Fisika' :  85,
    'Biologi' : 90,
    'Kimia' : 85,
    'PJOK' : 100,
    'PPKN' : 99,
}

def rata_rata():
    rata_nilai = np.mean(list(nilai_Eren.values()))
    print(f'Rata-rata nilai Eren: {rata_nilai}')
def maksimal():
    nilai_max = np.max(list(nilai_Eren.values()))
    print(f"Nilai maksimal Eren: {nilai_max}")
def minimal():
    nilai_min = np.min(list(nilai_Eren.values()))
    print(f"Nilai maksimal Eren: {nilai_min}")
def lolos():
    rata2 = np.mean(list(nilai_Eren.values()))
    if rata2 >= 75 :
        print("Selamat kamu lolos seleksi telyu")
    elif rata2 < 75:
        print("Silahkan coba lagi!")
    else: 
        print("Error")
rata_rata()
maksimal()
minimal()
lolos()
       

