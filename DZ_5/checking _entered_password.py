# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.

import hashlib

def get_hash_string(str):
    hash_str = hashlib.sha256(str.encode()).hexdigest()
    return f'Хэш введённого пароля: {hash_str}'

while True:
    password = input('введите пароль: ')
    if len(password) < 8:
        print('пароль менее 8 символов')
        continue
    if not any(char.isupper() for char in password):
        print('пароль должен содержать прописную букву')
        continue
    if not any(char.islower() for char in password):
        print('пароль должен содержать строчную букву')
        continue
    if not any(char.isdigit() for char in password):
        print('пароль должен содержать цифру')
        continue
    else:
        print('пароль плохой, попробуйте снова')
        break

print(get_hash_string(password))