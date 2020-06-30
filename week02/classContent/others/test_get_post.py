import requests

res = requests.get('https://github.com')
print(res.status_code)
print(res.headers['content-type'])
print(res.encoding)

postRes = requests.post('https://httpbin.org/post', data={'key': 'value'})
postRes.json()
