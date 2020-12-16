import random
import string

import requests

url = 'http://rnicr0s0ft0ficce893783.com/amz/1.php'

"""POST /amz/1.php HTTP/1.1
Host: rnicr0s0ft0ficce893783.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://9876543456886756565656-secondary.z19.web.core.windows.net/
Content-Type: application/x-www-form-urlencoded
Content-Length: 32
Origin: https://9876543456886756565656-secondary.z19.web.core.windows.net
Connection: keep-alive
Upgrade-Insecure-Requests: 1"""

'email=asdfasdf&Pass=sadfasdfasdf'

while True:
    randomuser = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 15))) + '@' + ''.join(
        random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 15))) + '.com'
    randompw = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(5, 30)))

    data = 'email=' + randomuser + '&Pass=' + randompw
    headers = {'Host': 'rnicr0s0ft0ficce893783.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate, br',
               'Referer': 'https://9876543456886756565656-secondary.z19.web.core.windows.net',
               'Content-Type': 'application/x-www -form-urlencoded',
               'Content-Length': 32,
               'Origin': 'https://9876543456886756565656-secondary.z19.web.core.windows.net',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': 1}
    requests.post(url, data, headers, allow_redirects=False)
    print(data)
