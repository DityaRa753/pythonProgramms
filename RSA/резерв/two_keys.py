# ШИФРОВАНИЕ RSA, чисто кортеж с цифрами.
# import rsa
# publicKey, privateKey = rsa.newkeys(2048)
# # print(file'Публичный ключ: {publicKey}\nПриватный ключ: {privateKey}',end='\n', sep='\n')
# message = b'Hello Blablacode.ru!'
# # шифруем
# crypto = rsa.encrypt(message, publicKey)
# print(crypto)
# # расшифровываем
# message = rsa.decrypt(crypto, privateKey)
# print(message)
#_____________________________

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
# Более правильный тип шифрования, т.к шифрует хеш.
# Генерация ключей для первого человека
privateKey = RSA.generate(2048) # На данный момент система шифрования на основе RSA считается надежной с размером ключа начиная от 2048 бит.
file = open('C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Приватный_ключ№1.txt','wb')
file.write(bytes(privateKey.exportKey('PEM'))); file.close()

publickey = privateKey.publickey()
file = open('C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Публичный_ключ№1.txt','wb')
file.write(bytes(publickey.exportKey('PEM'))); file.close()

# Генерация ключей для второго человека
privateKey = RSA.generate(2048)
file = open('C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Приватный_ключ№2.txt','wb')
file.write(bytes(privateKey.exportKey('PEM'))); file.close()
publickey = privateKey.publickey()
file = open('C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Публичный_ключ№2.txt','wb')
file.write(bytes(publickey.exportKey('PEM'))); file.close()
print('Ключи созданы, найти текстовики!')