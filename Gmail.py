# -*- coding: cp949 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
def htmlWrite(lst):
    html_txt='''<html>
    <header></header>
    <body>
    <b>��⵵ ����ȭ�� �ȳ��Դϴ�.</b><br>
    <img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MDVfMTIx/MDAxNTU0NDY5MjExMjU1.wqZPpUfUI8oQTRWmpokcbMbkfTJKAQTp7WrzyReQikcg.G6XmJwyR5uLc5AhCNwJnym6Rq-1qR4D6tqxOJvPvPRkg.PNG.odsej/ggmoney1.png?type=w800"/>
    '''

    html_txt+='<p>'+"��: "+lst[0]+'</p>'
    html_txt+='<p>'+"��ȣ��: "+lst[1]+'</p>'
    html_txt+='<p>'+"��������: "+lst[2]+'</p>'
    html_txt+='<p>'+"���θ� �ּ�: "+lst[3]+'</p>'
    html_txt+='<p>'+"�����ּ�: "+lst[4]+'</p>'
    html_txt+='<p>'+"��ȭ��ȣ: "+str(lst[5])+'</p>'
    html_txt+='<p>'+"�����ȣ: "+str(lst[6])+'</p>'
    html_txt+='<p>'+"����: "+str(lst[7])+'</p>'
    html_txt+='<p>'+"�浵: "+str(lst[8])+'</p>'

    html_txt+=''' </body>
    </html>'''
    html_file = open('logo.html', 'w')
    html_file.write(html_txt)
    html_file.close()


def SendMail(add):
    host = "smtp.gmail.com" # Gmail STMP ���� �ּ�.
    port = "587"
    htmlFileName = "logo.html"

    senderAddr = "ghdtnswh213@gmail.com"     # ������ ��� email �ּ�.
    recipientAddr = add               # �޴� ��� email �ּ�.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "�������ȭ�� ������ �ȳ�"

    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME ������ �����մϴ�.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
    htmlFD.close()

    # ������� mime�� MIMEBase�� ÷�� ��Ų��.
    msg.attach(HtmlPart)
    # ������ �߼��Ѵ�.
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)        # ������� �ʿ��� ��� �ּ��� Ǭ��.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("ghdtnswh213@gmail.com","****") #���⿡ ��й�ȣ ��� �ȴ�.
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()

