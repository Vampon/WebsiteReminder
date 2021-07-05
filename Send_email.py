from email.mime.text import MIMEText
import smtplib
def sendEmail(content):
    msg = MIMEText(content,'plain','utf-8')
    #发送邮箱地址
    from_addr = 'xxxxxx@qq.com'
    #邮箱授权码，非登陆密码
    password = 'xxxxxxxxx'
    #收件箱地址
    to_addr = "xxxxxx@qq.com,xxxxxx@qq.com"
    #smtp服务器
    smtp_server = 'smtp.qq.com'
    #发送邮箱地址
    msg['From'] = from_addr
    #收件箱地址
    msg['To'] = to_addr
    #主题
    msg['Subject'] = 'THE WEBSITE UPDATA!'
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    print(from_addr)
    print(password)
    server.login(from_addr,password)
    server.sendmail(from_addr, to_addr.split(','), msg.as_string())
    server.quit()