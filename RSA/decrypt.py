# from Crypto.PublicKey import RSA
# from Crypto.Random import get_random_bytes
# from Crypto.Cipher import AES, PKCS1_OAEP
# import os
# import sys

# @bot.message_handler(func=lambda message: True)
# def bot_dec(message: Message):
#     bot.reply_to(message, txt)
#     def decrypt(file):
#         file_in = open(file, "rb")
#         file_out = open(str(file[:-4]), "wb")
#         private_key = RSA.import_key(open(
#             "C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Private.pem").read())
#         enc_session_key, nonce, tag, ciphertext = \
#             [file_in.read(x)
#             for x in (private_key.size_in_bytes(), 16, 16, -1)]
#         file_in.close()  # была ошибка в файле, при расшифровке создавал новый, а старый не удалял как задумано, нужно было закрыть до os.remove т.к это удалило бы зашифрованный подлинник, но происходила ошибка, и она не удалялась. Допер сам частично, гугл в помощь... :) UDP: яркий пример поче нужно закрывать файлы, ВСЕГДА!
#         cipher_rsa = PKCS1_OAEP.new(private_key)
#         session_key = cipher_rsa.decrypt(enc_session_key)
#         cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
#         data = cipher_aes.decrypt_and_verify(ciphertext, tag)
#         file_out.write(data)
#         print(file + " decrypt")
#         os.remove(file)
#     def walk(dir):
#         for name in os.listdir(dir):
#             path = os.path.join(dir, name)
#             if os.path.isfile(path):
#                 decrypt(path)
#             else:
#                 walk(path)
#     # Запуск функции расшифровки.
#     walk("C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\test_crypt")
#     print("----------------------все файлы расшифрованы-----------------------------------------")

# bot.polling()
