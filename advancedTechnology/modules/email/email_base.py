#coding:utf-8

# coding=gbk
import smtplib, mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

msg = MIMEMultipart()
msg['From'] = "from@yeah.net"
msg['To'] = 'to@21cn.com'
msg['Subject'] = 'email for tesing'

# 添加邮件内容
txt = MIMEText("这是邮件内容~~")
msg.attach(txt)

# 添加二进制附件
fileName = r'F:\work\ipv6.txt'
ctype, encoding = mimetypes.guess_type(fileName)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)
att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype=subtype)
att1.add_header('Content-Disposition', 'attachment', filename=fileName)
msg.attach(att1)

# 发送邮件
mail_from = 'chen_jz06@126.com'
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(mail_from,'cjxPNXZX05')
smtp.sendmail(mail_from, '1667809009@qq.com', msg.as_string())
smtp.quit()
print('邮件发送成功')


