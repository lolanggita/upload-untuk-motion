import os

# Fungsi untuk menambahkan prefix pada file
def add_prefix_to_files(directory, prefix):
    for root, _, files in os.walk(directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, prefix + file)
            os.rename(old_file_path, new_file_path)

# Tentukan direktori dan prefix yang ingin digunakan
directory = "."  # Direktori saat ini
prefix = "Lola Anggita Citrawilis_102022300151_"

# Panggil fungsi untuk menambahkan prefix
add_prefix_to_files(directory, prefix)