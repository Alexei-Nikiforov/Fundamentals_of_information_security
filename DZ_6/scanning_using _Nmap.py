# Напишите программу на Python, которая будет проводить сканирование с использованием nmap

import nmap

def scan_host(host):
    # Создаем экземпляр сканера nmap
    nm = nmap.PortScanner()

    # Выполняем сканирование с помощью команды nmap -sn
    nm.scan(host, arguments='-sn')
    print(f'Результаты сканирования с помощью nmap -sn:\n{nm.csv()}\n')

    # Выполняем сканирование с помощью команды nmap -sO
    nm.scan(host, arguments='-sO')
    print(f'Результаты сканирования с помощью nmap -sO:\n{nm.csv()}\n')

    # Выполняем сканирование с помощью команды nmap --reason
    nm.scan(host, arguments='--reason')
    print(f'Результаты сканирования с помощью nmap --reason:\n{nm.csv()}\n')

if __name__ == '__main__':
    scan_host('127.0.0.1')