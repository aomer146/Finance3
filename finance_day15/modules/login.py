def login():
    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")
    if username == "admin" and password == "1234":
        print("✅ Giriş başarılı. Hoş geldiniz!")
        return True
    else:
        print("❌ Hatalı kullanıcı adı veya şifre.")
        return False
