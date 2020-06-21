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
    <b>경기도 지역화폐 안내입니다.</b><br>
    <img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MDVfMTIx/MDAxNTU0NDY5MjExMjU1.wqZPpUfUI8oQTRWmpokcbMbkfTJKAQTp7WrzyReQikcg.G6XmJwyR5uLc5AhCNwJnym6Rq-1qR4D6tqxOJvPvPRkg.PNG.odsej/ggmoney1.png?type=w800"/>
    '''

    html_txt+='<p>'+"시: "+lst[0]+'</p>'
    html_txt+='<p>'+"상호명: "+lst[1]+'</p>'
    html_txt+='<p>'+"업종종류: "+lst[2]+'</p>'
    html_txt+='<p>'+"도로명 주소: "+lst[3]+'</p>'
    html_txt+='<p>'+"지번주소: "+lst[4]+'</p>'
    html_txt+='<p>'+"전화번호: "+str(lst[5])+'</p>'
    html_txt+='<p>'+"우편번호: "+str(lst[6])+'</p>'
    html_txt+='<p>'+"위도: "+str(lst[7])+'</p>'
    html_txt+='<p>'+"경도: "+str(lst[8])+'</p>'

    html_txt+=''' </body>
    </html>'''
    html_file = open('logo.html', 'w')
    html_file.write(html_txt)
    html_file.close()


def SendMail(add):
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.html"

    senderAddr = "ghdtnswh213@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = add               # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "경기지역화폐 가맹점 안내"

    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
    htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)
    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("ghdtnswh213@gmail.com","****") #여기에 비밀번호 써야 된다.
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()

