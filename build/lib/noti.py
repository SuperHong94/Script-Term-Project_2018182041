#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback
import urllib.parse

TOKEN = '1087976724:AAFY3mVSbI2-1I30AYdEkgEuwTKF1AQwu9w'
MAX_MSG_LENGTH = 300
baseurl = 'https://openapi.gg.go.kr/RegionMnyFacltStus?KEY=2902618a276345c78da7557883182ca9'
bot = telepot.Bot(TOKEN)

def getData(cityName, storeName='',roadAddress="",localAddress=""):
    cityName = urllib.parse.quote(cityName)
    storeName = urllib.parse.quote(storeName)
    roadAddress = urllib.parse.quote(roadAddress)
    localAddress = urllib.parse.quote(localAddress)

    res_list = []
    url = baseurl+'&SIGUN_NM=' + cityName+"&CMPNM_NM="+storeName+"&(REFINE_ROADNM_ADDR="+roadAddress+"&REFINE_LOTNO_ADDR="+localAddress
    #print(url)
    res_body = urlopen(url).read()
    #print(res_body)
    soup = BeautifulSoup(res_body, 'html.parser')
    items = soup.findAll('row')
    for item in items:
        item = re.sub('<.*?>', '|', item.text)
        parsed = item.split('|')
        try:
            row = parsed[0]+'/'+parsed[3]+'/'+parsed[10]+'\n'
        except IndexError:
            row = item.replace('|', ',')

        if row:
            res_list.append(row.strip())

    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)

def run(date_param, param='11710'):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs( user TEXT, log TEXT, PRIMARY KEY(user, log) )')
    conn.commit()

    user_cursor = sqlite3.connect('users.db').cursor()
    user_cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    user_cursor.execute('SELECT * from users')

    for data in user_cursor.fetchall():
        user, param = data[0], data[1]
        print(user, date_param, param)
        res_list = getData( param, date_param )
        msg = ''
        for r in res_list:
            try:
                cursor.execute('INSERT INTO logs (user,log) VALUES ("%s", "%s")'%(user,r))
            except sqlite3.IntegrityError:
                # 이미 해당 데이터가 있다는 것을 의미합니다.
                pass
            else:
                print( r )
        if msg:
            sendMessage( user, msg )
    conn.commit()

if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current_month)
