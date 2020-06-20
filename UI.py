from tkinter import *
from tkinter.ttk import Combobox
import urllib.request
from xml.etree import ElementTree
from xml.dom.minidom import parse, parseString
import Search1
WIDTH=1200
HEIGHT=600
class MainGUI():
    def searchXML(self, cityName):
        cityCode = Search1.queryCode(cityName)

        for i in range(1, 100):
            url = "https://openapi.gg.go.kr/RegionMnyFacltStus?KEY=2902618a276345c78da7557883182ca9&pIndex=" + str(
                i) + "&pSize=500&SIGUN_CD=" + str(cityCode)
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            strXml = resp.read().decode('utf-8')
            if 'INFO-200' in strXml:
                break
            tree = ElementTree.fromstring(strXml)
            items = tree.iter("row")
            resutLst = []
            for j in items:
                rStr = []
                if j.find('SIGUN_NM').text:  # 시이름 0
                    rStr.append(j.find('SIGUN_NM').text)
                else:
                    rStr.append("정보 없음")

                if j.find('CMPNM_NM').text:  # 상점이름 1
                    rStr.append(j.find('CMPNM_NM').text)
                else:
                    rStr.append("정보 없음")

                if j.find('INDUTYPE_NM').text:  # 업종이름 2
                    rStr.append(j.find('INDUTYPE_NM').text)
                else:
                    rStr.append("정보 없음")

                if j.find('REFINE_ROADNM_ADDR').text:  # 도로명 주소 3
                    rStr.append(j.find('REFINE_ROADNM_ADDR').text)
                else:
                    rStr.append("정보 없음")

                if j.find('REFINE_LOTNO_ADDR').text:  # 지번 주소 4
                    rStr.append(j.find('REFINE_LOTNO_ADDR').text)
                else:
                    rStr.append("정보 없음")

                if j.find('TELNO').text:  # 전화 번호 5
                    rStr.append(j.find('TELNO').text)
                else:
                    rStr.append("정보 없음")

                if j.find('REFINE_ZIP_CD').text:  # 우편 번호 6
                    rStr.append(j.find('REFINE_ZIP_CD').text)
                else:
                    rStr.append("정보 없음")

                if j.find('REFINE_WGS84_LAT').text:  # 위도 7
                    rStr.append(j.find('REFINE_WGS84_LAT').text)
                else:
                    rStr.append("정보 없음")
                if j.find('REFINE_WGS84_LAT').text:  # 경도 8
                    rStr.append(j.find('REFINE_WGS84_LAT').text)
                else:
                    rStr.append("정보 없음")
                temp = ""
                for k in range(len(rStr)):
                    temp += (rStr[k] + "    ")

                self.listBox.insert(0,temp)




    def search(self):
        print(self.local.get())

        self.rLst=self.searchXML(self.local.get())






    def InitCityNames(self):
        self.local = StringVar()
        self.local.set("가평군")
        data = ["가평군", "고양시", "과천시", "광명시", "광주시", "구리시", "군포시", "김포시",
                "남양주시", "동두천시", "부천시", "성남시", "수원시", "시흥시", "안산시", "안성시", "안양시", "양주시",
                "양평군", "여주시", "연천군", "오산시", "용인시", "의왕시", "의정부시", "이천시", "파주시", "평택시", "포천시", "하남시", "화성시"]
        Combobox(self.searchFrame, values=data,textvariable=self.local,  font=("휴먼매직체",28),justify=RIGHT, width=30).grid(row=0,column=2)


    def __init__(self):
        self.window=Tk()
        self.window.title("경기도지역화페 가맹점 검색")
        self.window.geometry("1200x600")
        self.window.configure(background='lightBlue')

        self.rLst=[] #검색결과 리스트



        self.searchFrame=LabelFrame(self.window)
        self.searchFrame.grid(sticky=W+N,padx=5)
        Label(self.searchFrame,text="지역", font = ("휴먼매직체",30)).grid(row=0,column=1)
        Label(self.searchFrame,text="상호명", font = ("휴먼매직체",30)).grid(row=1,column=1)
        Label(self.searchFrame,text="업종", font = ("휴먼매직체",30)).grid(row=2,column=1)
        Label(self.searchFrame,text="도로명주소/지번주소", font = ("휴먼매직체",30)).grid(row=3,column=1)
        #self.local = StringVar() //함수로 잘되면 이부분 지우기
        #Entry(self.searchFrame, textvariable=self.local, font=("휴먼매직체", 30), justify=RIGHT, width=30).grid(row=0,column=2)
        self.InitCityNames()
        self.storeName = StringVar()
        Entry(self.searchFrame, textvariable=self.storeName, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=1, column=2)
        self.valueType = StringVar()
        Entry(self.searchFrame, textvariable=self.valueType, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=2, column=2)
        self.address = StringVar()
        Entry(self.searchFrame, textvariable=self.address, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=3, column=2)
        self.futureValue = StringVar()
        Label(self.searchFrame, textvariable=self.futureValue).grid(row=4, column=2, stick=E)

        Button(self.searchFrame, text="검색하기", font = ("휴먼매직체",20),command=self.search).grid(row=5, column=2, stick=E)

        #검색 결과  리스트박스 스크롤바가 있는 프레임
        self.resultFrame=LabelFrame(self.window,bg="white",width=WIDTH,height=HEIGHT/2)
        scrollbar = Scrollbar(self.resultFrame,width=17,bd=10)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar1 = Scrollbar(self.resultFrame, orient=HORIZONTAL, width=17, bd=10)
        scrollbar1.pack(side=BOTTOM, fill=X)
        self.listBox = Listbox(self.resultFrame, width=100, height=20, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
        self.listBox.insert(0,"dlkdkdkldl")
        self.listBox.pack(side="left")
        scrollbar["command"] = self.listBox.yview
        scrollbar1["command"] = self.listBox.xview
        self.resultFrame.grid(stick=W + S,padx=5)



        self.window.mainloop()




MainGUI()
