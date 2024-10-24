import sqlite3
import matplotlib.pyplot as plt

DATABASE_FILE = "karakter_anime.sqlite3"

def create_table():
    """Membuat table (dan database jika file belum ada)
    Args: None
    Output: Success message
    Returns: None
    """
    # Buat kode untuk membuat tabel anime pada database karakter_anime.sqlite3
    conn = sqlite3.connect("karakter_anime.sqlite3")
    cur = conn.commit()
    cur.execute("CREATE TABLE anime (id INTEGER not null primary key, nama TEXT not null, anime TEXT not null, power_level INTEGER not null, health INTEGER not null)")
    conn.commit()
    cur.close()
    

def insert_character(id, nama, anime, power_level, health):
    """Menyisipkan karakter baru ke dalam database
    Args:
        nama: str, nama karakter
        anime: str, judul anime
        power_level: float, tingkat kekuatan karakter
        health: int, tingkat kesehatan karakter
    Output: Success message
    Returns: None
    """
    # Buat kode untuk memasukkan 4 karakter legendaris secara otomatis ke dalam tabel anime
    conn = sqlite3.connect("karakter_anime.sqlite3")
    cur = conn.commit()
    cur.execute("""
                INSERT INTO anime (id, nama, anime, power_level, health)
                VALUES (?,?,?,?,?)""", (id, nama, anime, power_level, health))
    conn.commit
    cur.close()


def select_all_characters():
    """Mengambil dan mencetak semua karakter dari database
    Args: None
    Output: Informasi karakter dalam database
    Returns: None
    """
    # Buat kode untuk menampilkan isi dari semua tabel anime
    conn = sqlite3.connect("karakter_anime.sqlite3")
    cur = conn.commit()
    cur.execute("SELECT * FROM anime")
    result = conn.fetchall()
    cur.close()
    return(result)


def simulate_battle(character_id, enemy_id):
    """Mensimulasikan pertempuran antara karakter dengan musuh
    Args:
        character_id: int, id karakter yang menyerang
        enemy_id: int, id musuh yang diserang
    Output: Hasil pertempuran
    Returns: None
    """
    # Buat kode untuk mengambil informasi karakter yang menyerang (character_id) dan musuh yang diserang (enemy_id)
    conn = sqlite3.connect("karakter_anime.sqlite3")
    cur = conn.commit()
    cur.execute("SELECT * FROM anime")
    data = conn.fetchall()
    character_id = [anime[0:1] for anime in data]
    enemy_id = [anime[0:2] for anime in data]

    # Mengurangi health musuh berdasarkan power level karakter


    # Buat kode untuk mengupdate kesehatan musuh dalam database setelah


    # print hasil pertempuran


def visualize_health():
    """Visualisasi kesehatan karakter setelah semua pertarungan selesai dilakukan"""

   
    # Buat kode untuk menampilkan visualisasi (bar chart) dimana nama karakter di sumbu x dan tingkat kesehatan di sumbu y.


# Buat pemanggilan fungsi sesuai dengan operasi yang diminta pada soal latihan
create_table()
insert_character(1, 'Son Goku', 'Dragon Ball', 5000, 10000)
insert_character(2, 'Naruto Uzumaki', 'Naruto', 4000, 7500)
insert_character(3, 'Monkey D Luffy', 'One Piece', 3000, 6000)
insert_character(4, 'Ichigo Kurosaki', 'Bleach', 3500, 5000)
select_all_characters()