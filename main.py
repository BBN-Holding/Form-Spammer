import random
import string

import requests

url = 'https://adultadhdunplugged.com/update/ivian/doner/aws/login/submit.php'

while True:
    random_user = ''.join(
        random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 15))) + '@' + ''.join(
        random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 15))) + '.com'
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 30)))

    data = 'verbot=&type=login&email=' + random_user + '&password=' + random_password
    headers = {
        'authority': 'adultadhdunplugged.com',
        ':method': 'POST',
        ':path': '/update/ivian/doner/aws/login/submit.php',
        ':scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-DE;q=0.6',
        'cache-control': 'max-age=0',
        'content-length': '80',
        'content-type': 'application/x-www-form-urlencoded',
        'dnt': '1',
        'origin': 'https://adultadhdunplugged.com',
        'referer': 'https://adultadhdunplugged.com/update/ivian/doner/aws/login/login.php',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec - fetch - dest': 'document',
        'sec - fetch - mode': 'navigate',
        'sec - fetch - site': 'same - origin',
        'sec - fetch - user': '?1',
        'upgrade - insecure - requests': '1',
        'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    x = requests.post(url, data, headers, allow_redirects=False)
    print(x)
