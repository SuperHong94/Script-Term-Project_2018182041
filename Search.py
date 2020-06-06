# -*- coding:utf-8 -*-
import os
import sys
import http.client
import urllib.request
from xml.dom.minidom import parseString


client_id = "76gVHOGgqWwIyZsn3Mgl"
client_secret = "ZiO5RaxsRM"

#openAPI媛¢ https ��¦濡鬻�풰�黝�¦ �\ъK��린 ��臾몄�� HTTPSConnection ��¦ �\ъK�.
conn = http.client.HTTPSConnection("openapi.naver.com")
#conn.set_debuglevel(1) #debug mode �¦ㅼ��
headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
#encText = "love"
encText = urllib.parse.quote('한국산업기술대')  #한글검색할때
params = "?query=" + encText + "&display=10&start=1"
#isbn='0596513984'
#params = "?d_isbn="+isbn

conn.request("GET", "/v1/search/book.xml" + params, None, headers)
#conn.request("GET", "/v1/search/book_adv.xml" + params, None, headers) #상세검색

res = conn.getresponse()

if int(res.status) == 200 :
    print(parseString(res.read().decode('utf-8')).toprettyxml())
else:
    print ("HTTP Request is failed :" + res.reason)
    print (res.read().decode('utf-8'))

conn.close()