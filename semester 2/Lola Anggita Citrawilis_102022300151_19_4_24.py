def get_name_parts(name):

    name_parts = name.split()

    if len(name_parts) < 2 :
        raise ValueError("Nama harus mengandung Nama depan dan Nama belakang!")
    
    return name_parts[0], name_parts[-1]

while True:

    name = input("\nEnter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check email valid
    if not (email.endswith("@gmail.com") or email.endswith("@outlook.com")):
        print("Email tidak valid. Pendaftaran ditolak")
        continue

    # Check password meets requirements
    if len(password) < 8 or len(password) > 16 :
        print("Password harus memiliki panjang antara 8 dan 16 karakter!")
    
    elif not any(c.islower() for c in password) or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password):
        print("Password harus memiliki huruf kecil, huruf besar, dan angka!")
    
    else:
        first_name, last_name = get_name_parts(name)
        if password.count(first_name) > 0 or password.count(last_name) > 0 :
            print("Password tidak boleh mengandung nama awal atau akhir!")
        
        else:
            print("Pendaftaran diterima.")
    

    loop = input("Try new password? (y/n): ")

    if loop == "y" :
        pass
    elif loop == "n" :
        exit()

