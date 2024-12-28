# Напишите программу на Python, которая будет вычислять хэш-значения
# для введенного текста на sha256

from hashlib import sha256
input_ = input('Введите текст: ')
print(sha256(input_.encode('utf-8')).hexdigest())