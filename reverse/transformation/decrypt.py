# membaca file
enc = open("enc").read()
print(f"data: {enc}")
print("")
# membaca data dari index 0 dan dikonvert ke hex
print(f"konvert data ke hex: {hex(ord(enc[0]))}")
print("")
# loop setiap karakter dari enc
result = ""
for data in enc:
    data_hex = hex(ord(data)).lstrip("0x")
    result += data_hex
    hex_to_ascii = bytes.fromhex(result).decode('ascii')
print("hasil loop setiap char: ",result)
print("")
print("konvert hex ke ascii: ",hex_to_ascii)
