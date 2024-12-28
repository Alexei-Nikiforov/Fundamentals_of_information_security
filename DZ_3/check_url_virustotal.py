# Напишите программу на Python, которая будет взаимодействовать с API VirusTotal

import json
import requests

# ключ доступа от virustotal (*/)
apikey = "8f/d53367676279/f8f80bbddb7552260*feb2369285/9f06e32*3/6be12f913"

def scanurl(scan_url):
    url = "https://www.virustotal.com/api/v3/urls"
    payload = { "url": scan_url }
    headers = { "accept": "application/json", "x-apikey": apikey }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200: 
        id = response.json().get('data', '').get('id', '')
        # print(id)
        headers = { "accept": "application/json", "x-apikey": apikey }
        url = "https://www.virustotal.com/api/v3/analyses/" + id
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("Everything is OK")
            print(response.json())
        else:
            print("Error get request")
            print(response.status_code)
            print(response.json())
    else:
        print("Error post request")
        print(response.status_code)
        print(response.json())

scanurl("https://ya.ru")