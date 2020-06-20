
# -*- coding:utf-8 -*-
import urllib.request
from xml.etree import ElementTree
from xml.dom.minidom import parse, parseString
def queryCode(cityName):
    if cityName=="가평군":
        return 41820
    elif cityName=="고양시":
        return 41280
    elif cityName=="과천시":
        return 41290
    elif cityName=="광명시":
        return 41210
    elif cityName=="구리시":
        return 41310
    elif cityName=="고양시":
        return 41280
    elif cityName=="군포시":
        return 41410
    elif cityName=="김포시":
        return 41570
    elif cityName=="남양주시":
        return 41360
    elif cityName=="동두천시":
        return 41250
    elif cityName=="부천시":
        return 41190
    elif cityName=="성남시":
        return 41130
    elif cityName=="수원시":
        return 41110
    elif cityName=="시흥시":
        return 41390
    elif cityName=="안산시":
        return 41270
    elif cityName=="안성시":
        return 41550
    elif cityName=="안양시":
        return 41170
    elif cityName=="양주시":
        return 41630
    elif cityName=="양평군":
        return 41830
    elif cityName=="여주시":
        return 41670
    elif cityName=="연천군":
        return 41800
    elif cityName=="오산시":
        return 41370
    elif cityName=="용인시":
        return 41460
    elif cityName == "의왕시":
        return 41430
    elif cityName == "의정부시":
        return 41150
    elif cityName == "이천시":
        return 41500
    elif cityName == "파주시":
        return 41480
    elif cityName == "평택시":
        return 41220
    elif cityName == "포천시":
        return 41650
    elif cityName == "하남시":
        return 41450
    elif cityName == "화성시":
        return 41590

def extractBookData(strXml): #strXml은 OpenAPI 검색 결과 XML 문자열


    tree = ElementTree.fromstring(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.iter("row")    # item 엘리먼트 리스트 추출
    for i in itemElements:
        isbn = i.find("CMPNM_NM")          #isbn 검색
        if len(isbn.text) > 0 :
            return isbn.text # 사전형식 반환



def searchXML(self,cityName):

    cityCode=queryCode(cityName)
    resutLst=[]
    for i in range(1,100):
        url="https://openapi.gg.go.kr/RegionMnyFacltStus?KEY=2902618a276345c78da7557883182ca9&pIndex="+str(i)+"&pSize=500&SIGUN_CD="+str(cityCode)
        req=urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        strXml=resp.read().decode('utf-8')
        if 'INFO-200' in strXml:
            break
        tree=ElementTree.fromstring(strXml)
        items=tree.iter("row")
        rStr=[]
        for j in items :
            if j.find('SIGUN_NM').text: #시이름
                rStr.append(j.find('SIGUN_NM').text)
            else:
                rStr.append("정보 없음")

            if j.find('CMPNM_NM').text: # 상점이름
                rStr.append(j.find('CMPNM_NM').text)
            else:
                rStr.append("정보 없음")

            if j.find('INDUTYPE_NM').text: # 업종이름
                rStr.append(j.find('INDUTYPE_NM').text)
            else:
                rStr.append("정보 없음")

            if j.find('REFINE_ROADNM_ADDR').text: #도로명 주소
                rStr.append(j.find('REFINE_ROADNM_ADDR').text)
            else:
                rStr.append("정보 없음")

            if j.find('REFINE_LOTNO_ADDR').text: #지번 주소
                rStr.append(j.find('REFINE_LOTNO_ADDR').text)
            else:
                rStr.append("정보 없음")

            if j.find('TELNO').text: #전화 번호
                rStr.append(j.find('TELNO').text)
            else:
                rStr.append("정보 없음")

            if j.find('REFINE_ZIP_CD').text: #우편 번호
                rStr.append(j.find('REFINE_ZIP_CD').text)
            else:
                rStr.append("정보 없음")

            if j.find('REFINE_WGS84_LAT').text:  # 위도
                rStr.append(j.find('REFINE_WGS84_LAT').text)
            else:
                rStr.append("정보 없음")
            if j.find('REFINE_WGS84_LAT').text:  # 경도
                rStr.append(j.find('REFINE_WGS84_LAT').text)
            else:
                rStr.append("정보 없음")

        resutLst.append(rStr)





