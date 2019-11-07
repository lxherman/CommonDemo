import requests
import json
import random

def rand_ua():
    rand_ua_j = random.randint(0, 99)
    rand_ua_i = random.randint(100, 999)
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.%s.3770.%s Safari/537.36" % (
        rand_ua_j, rand_ua_i)
    return ua

api = 'http://www.winshangdata.com/api/ProjectMapApi.aspx'
headers = {
    'User-Agent': rand_ua(),
}

data = {
    "":"",
    "":""
}

proxies = {
    "http": "http://  ip  : port ",
    "https": "https://  ip  : port ",
}


# re = requests.get(api,headers=headers)
# re = requests.get(api,proxies=proxies)
re = requests.post(api,headers=headers,data=data)


print(re.text)
