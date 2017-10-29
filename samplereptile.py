#coding = utf-8
import requests
import requests_cache
import time
from bs4 import BeautifulSoup

#访问网页返回HTML页面
def url_open(url):
    # requests_cache.install_cache('demo_cache')
    headers = {
        'User-Agent' : 'Mozilla/5.0'
    }
    response = requests.get(url,headers = headers)
    response.encoding = 'gbk'
    response = response.text
    return response
#获取影片标题
def get_title(html_doc):
    soup = BeautifulSoup(html_doc, 'lxml')
    title = soup.find('h1')
    title = title.string
    return title


#获取影片下载路径
def get_download_url(html_doc):
    soup = BeautifulSoup(html_doc, 'lxml')
    td = soup.find('td',attrs={'style':'WORD-WRAP: break-word'})
    url_a = td.find('a')
    url_a = url_a.string
    return url_a


#主程序
def add_index_url(url,num,file_object):
    for i in range(1,num):
        new_url = url +str(i)+".html"
        print('----------------------当前爬取第'+str(i)+'页---------------------')
        html = url_open(new_url)
        time.sleep(1)
        soup = BeautifulSoup(html, 'lxml')
        a_urls = soup.select('.ulink')
        host = "http://www.ygdy8.net"
        for a_url in a_urls:
            a_url = host + a_url['href']
            print(a_url)
            html = url_open(a_url)
            write_title = get_title(html)
            write_url = get_download_url(html)
            file_object.write(write_title+"\n")
            file_object.write(write_url+"\n\n")

if __name__=="__main__":
    url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_"
    filename = "down_load_url.txt"
    num = int(input('请输入你要爬取的页数：'))
    num = num +1
    with open(filename ,'w') as file_object:
        add_index_url(url,num,file_object)
    print('----------------------爬取完成--------------------------')
    file_object.close()










