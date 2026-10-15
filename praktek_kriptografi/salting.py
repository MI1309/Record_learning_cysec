import bcrypt

# -------------------------------------------------------------
# 1. SAAT USER MENDAFTAR (REGISTER / BUAT PASSWORD)
# -------------------------------------------------------------
password_user = input("passwrd : ")

# Langkah A: Ubah string password ke bentuk Bytes
password_bytes = password_user.encode('utf-8')
print(f"Password dalam bentuk Bytes: {password_bytes}")

# Langkah B: Generate SALT acak yang aman secara kriptografi
# gensalt() secara otomatis membuat salt acak 128-bit
salt = bcrypt.gensalt(rounds=12)  # rounds=12 adalah Work Factor (Cost)
print(f"Salt acak yang dibuat : {salt.decode('utf-8')}")

# Langkah C: Gabungkan Password + Salt lalu di-Hash
hashed_password = bcrypt.hashpw(password_bytes, salt)
print(f"Hasil Hash di Database: {hashed_password.decode('utf-8')}")


# -------------------------------------------------------------
# 2. SAAT USER LOGIN (VERIFIKASI PASSWORD)
# -------------------------------------------------------------
password_input_login = input("password : ")  # User mengetik password saat login
input_bytes = password_input_login.encode('utf-8')

# Pustaka bcrypt secara otomatis mengekstrak Salt dari hashed_password yang disimpan,
# lalu meng-hash input_bytes dengan Salt tersebut untuk dicocokkan.
if bcrypt.checkpw(input_bytes, hashed_password):
    print("\n✅ Login Berhasil! Password cocok.")
else:
    print("\n❌ Login Gagal! Password salah.")