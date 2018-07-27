#coding:utf-8


import smtplib

smtp = smtplib.SMTP()
smtp.set_debuglevel(debuglevel='debug')
smtp.connect("smtp.qq.com", "25")
smtp.login('1667809009@qq.com', 'cjx_886')
smtp.sendmail('1667809009@qq.com', 'chen_jz06@126.com',
              'From: from@yeah.net/r/nTo: to@21cn.com/r/nSubject: this is a email from python demo/r/n/r/nJust for test~_~')
smtp.quit()
"""
smtplib.SMTP([host[, port[, local_hostname[, timeout]]]])
SMTP类构造函数，表示与SMTP服务器之间的连接，通过这个连接我们可以向smtp服务器发送指令，执行相关操作（如：登陆、发送邮件）。该类提供了许多方法，将在下面介绍。它的所有参数都是可选的，其中host参数表示smtp服务器主机名，上面例子中的smtp主机为”smtp.yeah.net”；port表示smtp服务的端口，默认是25；如果在创建SMTP对象的时候提供了这两个参数，在初始化的时候会自动调用connect方法去连接服务器。
smtplib模块还提供了SMTP_SSL类和LMTP类，对它们的操作与SMTP基本一致。
smtplib.SMTP提供的方法：
?
1
SMTP.set_debuglevel(level)
设置是否为调试模式。默认为False，即非调试模式，表示不输出任何调试信息。
?
1
SMTP.connect([host[, port]])
连接到指定的smtp服务器。参数分别表示smpt主机和端口。注意: 也可以在host参数中指定端口号（如：smpt.yeah.net:25），这样就没必要给出port参数。
?
1
SMTP.docmd(cmd[, argstring])
向smtp服务器发送指令。可选参数argstring表示指令的参数。下面的例子完全通过调用docmd方法向服务器发送指令来实现邮件的发送

"""


"""
SMTP.helo([hostname])
使用”helo”指令向服务器确认身份。相当于告诉smtp服务器“我是谁”。
SMTP.has_extn(name)
判断指定名称在服务器邮件列表中是否存在。出于安全考虑，smtp服务器往往屏蔽了该指令。
SMTP.verify(address)
判断指定邮件地址是否在服务器中存在。出于安全考虑，smtp服务器往往屏蔽了该指令。
SMTP.login(user, password)
登陆到smtp服务器。现在几乎所有的smtp服务器，都必须在验证用户信息合法之后才允许发送邮件。
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
发送邮件。这里要注意一下第三个参数，msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。在上面的例子中，msg的值为：
 
'''''From: from@yeah.net 
To: to@21cn.com 
Subject: test 
  
just for test'''
"""






