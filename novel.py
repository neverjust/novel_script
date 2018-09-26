import re
import smtplib
from bs4 import BeautifulSoup
import requests
from email.mime.text import MIMEText
import os
class novel(object):
    url = "https://www.23us.so/files/article/html/"
    page_place = os.path.abspath('..') + "/page.txt"
    sender = 'xxxian1999@126.com'
    pwd = 'xxxian1999'
    receiver = '312726839@qq.com'
    mail_host = 'smtp.126.com'
    book_tags = [
    '6/6276/',#秘诡之主
    '22/22791/',#克斯玛帝国
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    def __init__(self):
        books = [];
        for i in novel.book_tags:
            books.append(novel.url+i);


    def get_newest(self,url):
        url = url + '\d+.html'
        file = open(self.page_place, "r+")
        content = file.read()
        new_url = re.search(url, content).group(0)
        return new_url

    #判断这个url是不是最新的
    #是返回false
    #有更新返回最新的url
    def check_newest(self,url):
        response = requests.get(url).content
        page = BeautifulSoup(response,'html.parser').find_all('a')
        if (page[-2].get('href') == page[-3].get('href')):
            return False
        else:
            new_url = "https://www.23us.so"+ page[-2].get('href')
            file = open(self.page_place, "r+")
            content = file.read().replace(url,new_url)
            file.seek(0,0)
            file.write(content)
            return "https://www.23us.so"+ page[-2].get('href')



    def send(self,url):
        response = requests.get(url).content
        page = BeautifulSoup(response, 'html.parser')
        temp = page.title.get_text().split()
        title = temp[0]+' ' + temp[2].split('-')[0]
        content = page.find_all(id='contents')[0].get_text()

        email = smtplib.SMTP_SSL()
        message = MIMEText(content,'plain', 'utf-8')
        message['From'] = self.sender # 发送者
        message['To'] = self.receiver  # 接收者
        message['Subject'] = title

        email.connect(self.mail_host,465)
        email.login(self.sender,self.pwd)
        email.sendmail(self.sender,self.receiver,message.as_string())
        email.quit()



    def run(self):
        for novel in self.book_tags:
            book_tag = self.url + novel
            url_old = self.get_newest(book_tag)
            res = self.check_newest(url_old)
            if res == False:
                continue
            else:
                self.send(res)


if __name__ == '__main__':
    obj = novel()
    obj.run()

