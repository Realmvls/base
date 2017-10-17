#!/usr/bin/Python
# -*- coding: utf-8 -*-
#未完待续
import requests
from lxml import etree
url = 'https://www.hao123.com/'
html = requests.get(url).text             #response 和 str对象均无xpath属性
# print(html)
select = etree.HTML(html)
content = select.xpath('//a[@class=link g-fc20h]')
for data in content:
    print(data)
