#coding = utf-8
import requests
import requests_cache
import time
from bs4 import BeautifulSoup
import re


#访问网页返回HTML页面
def url_open(url):
    requests_cache.install_cache('demo_cache')
    headers = {
        'User-Agent' : 'Mozilla/5.0'
    }
    response = requests.get(url,headers = headers)
    response.encoding = 'utf8'
    response = response.text
    pattern = re.compile(r'<div class="article block untagged mb15[\s\S]*?class="stats-vote"[\s\S]*?</div>', re.S)
    contents = re.findall(pattern, response)
    return response

def add_index_url(url,num,file_object):
    for i in range(1,num):
        new_url = url +str(i)
        print('----------------------当前爬取第'+str(i)+'页---------------------')
        html = url_open(new_url)
        time.sleep(1)
        soup = BeautifulSoup(html, 'lxml')
        contents = soup.select('.content')
        for content in contents:
            content = re.sub(r'\n|<div class="content">|<span>|</span>|<br/> |</div>|</div> |\n\n', '', str(content))
            content = content.replace("<br/>","")
            file_object.write(content + "\n\n")




if __name__=="__main__":
    url = "http://www.qiushibaike.com/text/page/"
    filename = "CSBK.txt"
    num = int(input('请输入你要爬取的页数：'))
    num = num +1
    with open(filename ,'w') as file_object:
        add_index_url(url,num,file_object)
    print('----------------------爬取完成--------------------------')
    file_object.close()