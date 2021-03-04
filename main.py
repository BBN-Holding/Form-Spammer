import random
import string

import requests

url = 'https://innovairgroup-casemed.tk/hotmail/maureen.php'

while True:
    random_user = ''.join(
        random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 15))) + '@bbn.one'
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 30)))

    data = 'email=' + random_user + '&password=' + random_password
    headers = {':authority': 'innovairgroup-casemed.tk',
               ':method': 'POST',
               ':path': '/hotmail/maureen.php',
               ':scheme': 'https',
               'accept': 'application/json, text/javascript, */*; q=0.01',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-DE;q=0.6',
               'cache-control': 'no-cache',
               'content-length': '36',
               'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'dnt': '1',
               'origin': 'https://peppermint-cooperative-mantis.glitch.me',
               'pragma': 'no-cache',
               'referer': 'https://peppermint-cooperative-mantis.glitch.me/',
               'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
               'sec-ch-ua-mobile': '?0',
               'sec-fetch-dest': 'empty',
               'sec-fetch-mode': 'cors',
               'sec-fetch-site': 'cross-site',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36}',
               }
    requests.post(url, data, headers, allow_redirects=False)
    print(data)
