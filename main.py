import random
import string

import requests

url = 'INSERT URL'

while True:
    random_user = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 15))) + '@' + ''.join(
        random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 15))) + '.com'
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 30)))

    data = 'email=' + random_user + '&Pass=' + random_password
    headers = {'Host': 'INSERT DOMAIN',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/x-www -form-urlencoded',
               'Content-Length': 32,
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': 1}
    requests.post(url, data, headers, allow_redirects=False)
    print(data)
