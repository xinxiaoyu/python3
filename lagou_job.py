#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from lxml import etree
import lxml

origin = 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%BF%90%E7%BB%B4%E5%B7%A5%E7%A8%8B%E5%B8%88'
user_agent = ('User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
              '(KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')
headers = {
           'origin': origin,
           'User-Agent': user_agent,
           }

r = requests.get(url=origin, headers=headers)

soup = BeautifulSoup(r.content, 'lxml')


for item in soup.find_all('a', id='tab_pos', class_='active', rel='nofollow', href='javascript:;'):
	print(item.span)
