import requests
import time
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
user_agent = ua.random

headers = {'User-Agent': user_agent,
           'Referer': 'https://accounts.douban.com/passport/login?redir=https://accounts.douban.com/passport/setting'}

data = {'ck': '',
        'name': 'xxxx',
        'password': 'xxxx',
        'remember': 'false',
        'ticket': ''}

s = requests.Session()

preRes = s.get('https://accounts.douban.com/passport/login', headers=headers)

res = s.post('https://accounts.douban.com/j/mobile/login/basic', data=data,
             headers=headers, cookies=preRes.cookies)

print(res.status_code)
print(res.json())

time.sleep(5)

settingUrl = 'https://accounts.douban.com/passport/setting'

headers['Referer'] = 'https://www.douban.com/'

res = s.get(settingUrl, headers=headers)

print(res.status_code)

with open('profile.html', 'w+') as f:
    f.write(res.text)
