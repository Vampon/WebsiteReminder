import urllib.request
import re
import datetime
import pymysql
from bs4 import BeautifulSoup
from lxml import etree
import os
import json
from Send_email import sendEmail
import numpy as np

class SaveJson(object):
    def save_file(self, path, item):
        # 先将字典对象转化为可写入文本的字符串
        item = json.dumps(item,ensure_ascii=False)
        try:
            if not os.path.exists(path):
                with open(path, "w", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("write success")
            else:
                with open(path, "a", encoding='utf-8') as f:
                    f.write(item + ",\n")
                    print("write success")
        except Exception as e:
            print("write error==>", e)


# 爬虫，抓取官网信息
def infojyt(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    result = {}
    indexURL='http://yzb.hit.edu.cn'
    req = urllib.request.Request(url, headers=headers)
    # content = req.text   #获取网站源码
    response = urllib.request.urlopen(req)
    HTML = response.read().decode("utf-8")
    soup = BeautifulSoup(HTML, 'lxml')
    pat = r'<recordset>(.*?)</recordset>'
    re_jytinfo = re.search(
        r'<ul\s?class="wp_article_list_table">(?P<wp_article_list_table>.+?)<ul class="wp_article_list_table">', HTML
    )
    for tag in soup.find_all('span', class_='aa1'):
        t = tag.find('a')
        m_title = t.get_text()
        m_url = indexURL + t.get('href')
        # 加载存档数据
        read_dictionary = np.load('title.npy', allow_pickle=True).item()
        # 发现数据更新
        if m_title not in read_dictionary:
            result[m_title] = m_url
            print('WEBSITE UNDATA!')
            # 更新数据存入文件
            np.save('title.npy', result)
            print(result)
            sendEmail("您关注的网站更新了文章"+m_title+'\n'+"文章链接为"+m_url)


        # json存储模块 待开发
        #path = "test.json"
        #s = SaveJson()
        # if not os.path.isfile("test.json"):
        #    s.save_file(path, result)
        #    print('FILE CREATE!')
        #    print('------')
        # else:
        #    compara=[]
        #    file = open('test.json','r',encoding='UTF-8')
        #    #for line in file.readlines():
        #        #将json格式的数据映射成list的形式
        #    #    JSON_Data = json.loads(line)
        #    #    compara.append(JSON_Data)


if __name__ == '__main__':
    url = "http://yzb.hit.edu.cn/8822/list.htm"
    info = infojyt(url)







