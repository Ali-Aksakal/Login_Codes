import sqlite3
import logging

logging.basicConfig(filename='user_login.log',level=logging.INFO,format='%(asctime)s - %(message)s')


def login(user_nickname, password):
    with sqlite3.connect("register_table.db") as vt: # Veritabanı bağlantısını kur
        im = vt.cursor()

        im.execute("SELECT * FROM users WHERE user_nickname=? AND password=?", (user_nickname, password))
        if im.fetchone():
            print("Giriş başarılı!")
            logging.info(f"{user_nickname} kullanıcısı başarıyla giriş yaptı.")  # Giriş zamanını kaydet
        else:
            print("Hatalı kullanıcı adı veya şifre.")
            logging.warning(f"{user_nickname} kullanıcısı hatalı giriş denemesi yaptı.")  # Hatalı giriş zamanını kaydet

        vt.commit()

while True:
    print("\nHoş geldiniz!")
    print("1. Giriş Yap")
    print("2. Kayıt Ol")
    print("3. Çıkış")
    choice = input("Seçiminizi yapın: ")

    if choice == '1':
        user_nickname = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        login(user_nickname, password)
    elif choice == '2':
        break  # kayıt sayfasına geçiş için bağlantı oluşturulur
    elif choice == '3':
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")