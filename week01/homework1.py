import requests
import random
import pandas as pd

from bs4 import BeautifulSoup as bs


def get_url(url):
    user_agents = [
        'Mozilla/5.0 (Windows U Windows NT 6.1 en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50']

    user_agent = random.choice(user_agents)

    # print(user_agent)

    headers = {'user-agent': user_agent}
    response = requests.get(url, headers=headers)

    bs_info = bs(response.text, 'html.parser')

    # print(bs_info)

    divstag = bs_info.find_all(
        'div', attrs={'class': 'movie-item-hover'}, limit=10)

    res = []

    for divtag in divstag:
        fname = divtag.find('span', attrs={'class': 'name'}).text
        ftype, fdate = '', ''

        for span in divtag.find_all('span', attrs={'class': 'hover-tag'}):
            txt = span.text
            if txt == '类型:':
                ftype = span.next_sibling
            if txt == '上映时间:':
                fdate = span.next_sibling
        print(fname, ftype, fdate)
        res.append([fname.strip(), ftype.strip(), fdate.strip()])

    return res


url = 'https://maoyan.com/films?showType=3'

mylist = get_url(url)

print(mylist)
movies = pd.DataFrame(data=mylist)
movies.to_csv('./movie.csv', encoding='utf8', index=False, header=False)
