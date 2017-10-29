#coding = utf-8
import requests
import requests_cache
import time
from bs4 import BeautifulSoup
import re
import urllib.request


def url_open(url):
    requests_cache.install_cache('demo_cache')
    headers = {
        'User-Agent' : 'Mozilla/5.0'
    }
    response = requests.get(url,headers = headers)
    response.encoding = 'gbk'
    response = response.text
    return response

def getImg(url,num):
    for i in range(1, num):
        print('----------------------当前爬取第' + str(i) + '页---------------------')
        new_url = url + str(i) + ".html"
        html=url_open(new_url)
        titles = gettitle(html)
        pattern = re.compile('src="(.+?.gif)" style')
        gifs = re.findall(pattern, html)
        x = 0
        for gif in gifs:
            title = titles[x].string
            urllib.request.urlretrieve(gif, 'f:\\demo\%s.gif' % title)
            print("第"+str(x+1)+"张")
            x+=1


def gettitle(html):
    soup = BeautifulSoup(html,'lxml')
    list = soup.find_all('div',class_='mtitle')
    return list




url = "http://www.qiubaichengren.com/gif/list_"
num = int(input('请输入你要爬取的页数：'))
num = num + 1
html = getImg(url,num)
print('----------------------爬取完成--------------------------')