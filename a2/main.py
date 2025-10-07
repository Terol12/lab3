import string

password = input("Введите пароль: ")

errors = []

if len(password) != 8:
    errors.append("Длина пароля не равна 8")

if password.lower() == password:
    errors.append("В пароле отсутствуют заглавные буквы")

if password.upper() == password:
    errors.append("В пароле отсутствуют строчные буквы")

if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")

special_symbols = "*-#"
if not any(symbol in special_symbols for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")

allowed_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "*-#"
if not all(symbol in allowed_chars for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")

if errors:
    for error in errors:
        print(error)
else:
    print("Надежный пароль")