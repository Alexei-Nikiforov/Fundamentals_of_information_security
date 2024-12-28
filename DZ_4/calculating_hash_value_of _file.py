# Напишите программу на Python, которая будет вычислять хэш-значения
# для введенного пути файла и алгоритма хэша

import hashlib

def compute_file_hash(file_path, algorithm='sha256'):
    # Вычислить хэш файла с использованием указанного алгоритма
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def main():
    file_path = input("Введите путь к файлу: ")
    algorithm = input("Введите алгоритм хэша (например, md5, sha1, sha256): ")
    try:
        file_hash = compute_file_hash(file_path, algorithm)
        print(f"Хэш файла {file_path} по алгоритму {algorithm} равен: {file_hash}")
    except FileNotFoundError:
        print("Файл не найден. Введите правильный путь к файлу.")
    except ValueError:
        print(f"Недопустимый алгоритм хэширования: {algorithm}. Введите правильный алгоритм (например, md5, sha1, sha256).")

if __name__ == "__main__":
    main()