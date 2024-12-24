import random
import string


def generatePassword(length):
    # Проверка на допустимую длину
    if length < 1 or length > 25:
        raise ValueError("Password length must be between 1 and 25.")

    # Генерация пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    # Разделение пароля на строки по 15 символов
    return '\n'.join(password[i:i + 15] for i in range(0, len(password), 15))
