from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Private.pem", "wb")
file_out.write(private_key)
print(private_key)

public_key = key.publickey().export_key()
file_out = open("C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Public.pem", "wb")
file_out.write(public_key)
print(public_key)
# запишет в формате .pem можно открыть как txt
