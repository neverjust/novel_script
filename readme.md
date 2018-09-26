#看小说的脚本
####服务器爬取小说最新章节并发送邮件到手机脚本
####爬取源 顶点小说网(https://www.23us.so)
###使用方法
+ 在novel.py脚本里修改配置L
    '''url = "https://www.23us.so/files/article/html/"
    sender = ''
    pwd = ''
    receiver = ''
    mail_host = '' #授权码
    book_tags = [
    '6/6276/',#秘诡之主
    '22/22791/',#克斯玛帝国
    ]
    '''
+ 在page.txt里加上想看小说最新章节的url
+ 挂到服务器上之后 用cron定时每分钟运行一次
    > crontab -e 
    > > */1 * * * * python 脚本绝对路径