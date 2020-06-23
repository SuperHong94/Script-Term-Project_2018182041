from tkinter import *
import tkinter.ttk
from tkinter.ttk import Combobox
import urllib.request
from xml.etree import ElementTree
from tkinter.ttk import Treeview
from Gmail import *
from xml.dom.minidom import parse, parseString
import folium
import webbrowser
import spam
import random


WIDTH=1200
HEIGHT=600
class MainGUI():
    def Selectclick(self,e):
        self.canvas.delete('all')
        self.selectResult = self.treeview.item(self.treeview.selection()[0])

        self.canvas.create_text(200,30+20*0,text="시 :"+str(self.selectResult['values'][0]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*1,text="상호명 :"+str(self.selectResult['values'][1]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*2,text="업종종류 :"+str(self.selectResult['values'][2]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*3,text="도로명 주소 :"+str(self.selectResult['values'][3]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*4,text="지번주소 :"+str(self.selectResult['values'][4]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*5,text="전화번호 :"+str(self.selectResult['values'][5]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*6,text="우편번호 :"+str(self.selectResult['values'][6]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*7,text="위도 :"+str(self.selectResult['values'][7]).strip(),font=("나눔고딕코딩", 10))
        self.canvas.create_text(200,30+20*8,text="경도 :"+str(self.selectResult['values'][8]).strip(),font=("나눔고딕코딩", 10))
        self.mapButton['state'] = 'active'
        self.mailButton['state'] = 'active'
    def InitTreeView(self):
        self.resultFrame = LabelFrame(self.MainFrame1, bg="white", width=100, height=HEIGHT / 2)
        scrollbar = Scrollbar(self.resultFrame, width=17, bd=10)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar1 = Scrollbar(self.resultFrame, orient=HORIZONTAL, width=17, bd=10)
        scrollbar1.pack(side=BOTTOM, fill=X)
        # self.listBox = Listbox(self.resultFrame, width=100, height=20, yscrollcommand=scrollbar.set,xscrollcommand=scrollbar1.set)
        # self.listBox.pack(side="left")
        # scrollbar["command"] = self.listBox.yview
        # scrollbar1["command"] = self.listBox.xview
        self.treeview = Treeview(self.resultFrame, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar1.set,
                                 columns=["1", "2", "3", "4", "5", "6", "7", "8", "9"])

        self.treeview.column("#0", width=50)
        self.treeview.heading("#0", text="번호")
        self.treeview.column("#1", width=100)
        self.treeview.heading("#1", text="시", anchor='center')
        self.treeview.column("#2", width=100)
        self.treeview.heading("#2", text="상호명", anchor='center')
        self.treeview.column("#3", width=100)
        self.treeview.heading("#3", text="업종종류", anchor='center')
        self.treeview.column("#4", width=100)
        self.treeview.heading("#4", text="도로명주소", anchor='center')
        self.treeview.column("#5", width=100)
        self.treeview.heading("#5", text="지번주소", anchor='center')
        self.treeview.column("#6", width=100)
        self.treeview.heading("#6", text="전화번호", anchor='center')
        self.treeview.column("#7", width=90)
        self.treeview.heading("#7", text="우편번호", anchor='center')
        self.treeview.column("#8", width=90)
        self.treeview.heading("#8", text="위도", anchor='center')
        self.treeview.column("#9", width=100)
        self.treeview.heading("#9", text="경도", anchor='center')

        self.treeview.bind("<Double-1>", self.Selectclick) #더블클릭하면 이벤트

        #self.resultFrame.grid(stick=W + S, padx=5)
        self.resultFrame.grid(row=1,column=0, padx=5,pady=5,sticky=W)
        self.treeview.pack(side='left', fill=X)
        scrollbar["command"] = self.treeview.yview
        scrollbar1["command"] = self.treeview.xview

        pass
    def searchXML(self, cityName,storeName="",roadAddress="",localAddress=""):
        #self.listBox.delete(0,"end")
        self.treeview.delete(*self.treeview.get_children())

        cityCode = spam.queryCode(cityName.split('/')[1])

        cnt=0
        #encText = urllib.parse.quote("부천시")
        storeName=urllib.parse.quote(storeName)
        roadAddress=urllib.parse.quote(roadAddress)
        localAddress=urllib.parse.quote(localAddress)

        for i in range(1, 100): #원래 100에 1000개많큼 읽기
            url = "https://openapi.gg.go.kr/RegionMnyFacltStus?KEY=2902618a276345c78da7557883182ca9&pIndex=" + str(
                i) + "&pSize=1000&SIGUN_CD=" + str(cityCode)+"&CMPNM_NM="+storeName+"&(REFINE_ROADNM_ADDR="+roadAddress+"&REFINE_LOTNO_ADDR="+localAddress
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            strXml = resp.read().decode('utf-8')
            if 'INFO-200' in strXml:
                break
            tree = ElementTree.fromstring(strXml)
            items = tree.iter("row")
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
                if j.find('REFINE_WGS84_LOGT').text:  # 경도 8
                    rStr.append(j.find('REFINE_WGS84_LOGT').text)
                else:
                    rStr.append("정보 없음")
                temp = ""
                tuple(rStr)
                self.treeview.insert("",'end', text=str(cnt), values=rStr, iid=str(cnt) + "번")
                cnt += 1

                '''for k in range(len(rStr)):

                    temp += (rStr[k] + "    ")
                cnt += 1
                self.listBox.insert("end",str(cnt)+"    "+temp)'''



    def search(self):
        self.mapButton['state']='disable'
        self.rLst=self.searchXML(self.local.get(),storeName=self.storeName.get(),
                                 roadAddress=self.roadAddress.get(),localAddress=self.localAddress.get()) #storeName="",storeType="",roadAddress=""

    def SearchMap(self):
        # 위도 경도 지정
        x=eval(self.selectResult['values'][7])
        y=eval(self.selectResult['values'][8])
        map_osm = folium.Map(location=[x, y], zoom_start=13)

        folium.Marker([x, y], popup=self.selectResult['values'][1]).add_to(map_osm)

        map_osm.save('osm.html')
        webbrowser.open_new('osm.html')

    def sendMail(self):
        address=self.mailAdress.get()
        if address=="":
            self.mailAdress.set("여기에 메일주소를 꼭 넣어야 메일 보낼 수 있어요")
        htmlWrite(self.selectResult['values'])
        SendMail(address)


    def InitCityNames(self):
        self.local = StringVar()
        self.local.set("가평군/Gapyeong")
        data = ["가평군/Gapyeong", "고양시/Goyang", "과천시/Gwacheon", "광명시/Gwangmyeong", "광주시/Gwangju", "구리시/Guri",
                "군포시/Gunpo", "김포시/Gimpo",
                "남양주시/Namyangju", "동두천시/Dongducheon", "부천시/Bucheon", "성남시/Seongnam", "수원시/Suwon",
                "시흥시/Siheung", "안산시/Ansan", "안성시/Anseong", "안양시/Anyang", "양주시/Yangju",
                "양평군/Yangpyeong", "여주시/Yeoju", "연천군/Yeoncheon", "오산시/Osan", "용인시/Yongin", "의왕시/Uiwang",
                "의정부시/Uijeongbu", "이천시/Icheon", "파주시/Paju", "평택시/Pyeongtaek", "포천시/Pocheon", "하남시/Hanam",
                "화성시/Hwaseong"
                ]
        Combobox(self.searchFrame, values=data,textvariable=self.local,  font=("휴먼매직체",28),justify=RIGHT, width=30).grid(row=0,column=2)

    def DrawGraph(self):
        self.FrameName['text'] = self.local1.get() + " 월별 지역화폐 카드 사용량 비교"
        result = []
        # == 결과 가져오기
        cityName = self.local1.get() #local1은 그래프
        cityCode = spam.queryCode(cityName.split('/')[1])

        url = "https://openapi.gg.go.kr/RegionMnyPublctUse?KEY=67a6b558f57643aca2706cc7b8a40bb7&pIndex=1&pSize=1000&SIGUN_CD=" + str(cityCode)

        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        strXml = resp.read().decode('utf-8')
        tree = ElementTree.fromstring(strXml)
        items = tree.iter("row")

        for j in items:
            rStr = []
            if j.find('CARD_USE_AMT').text!=None:  # 사용량
                if j.find('STD_YM').text:  # 날짜
                    if (j.find('STD_YM').text).split('-')[1]>'06':
                        rStr.append('2019-'+j.find('STD_YM').text.split('-')[1])
                    else:
                        rStr.append(j.find('STD_YM').text)
                if j.find('SIGUN_NM').text:  # 시이름 0
                    rStr.append(j.find('SIGUN_NM').text)
                if j.find('CARD_USE_AMT').text:  # 사용량
                    rStr.append(j.find('CARD_USE_AMT').text)

                temp=tuple(rStr)
                result.append(temp)

        result=list(set(result))
        result.sort() #정보 뽑아내기 성공!
        counts = [eval(result[x][2]) for x in range(len(result))]
        maxCount=max(counts) #가장 높은 값 뽑아내기

        HEIGHT=400
        rangeValue=len(counts)
        barWidth = (1200 - rangeValue) / rangeValue  # 1개 막대그래프의 너비

        self.graphCanvas.delete('histogram')
        for i in range(rangeValue):
            color = '{:06x}'.format(random.randint(0, 0x1000000))
            self.graphCanvas.create_rectangle(50 + i * barWidth, (HEIGHT - (HEIGHT - 80) * (counts[i] / maxCount))-40,
                                             50+ (i + 1) * barWidth, HEIGHT-20,fill=('#'+color), tags='histogram')
            self.graphCanvas.create_text(100 + i * barWidth, (HEIGHT - (HEIGHT - 80) * counts[i] / maxCount) - 50,
                                        text=str(counts[i]), tags='histogram')
            self.graphCanvas.create_text(100 + i * barWidth, HEIGHT-10,
                                         text=str(result[i][0]), tags='histogram')


    def InitGraph(self):

        self.local1 = StringVar()
        self.local1.set("가평군/Gapyeong")
        data = ["가평군/Gapyeong", "고양시/Goyang", "과천시/Gwacheon", "광명시/Gwangmyeong", "광주시/Gwangju", "구리시/Guri",
                "군포시/Gunpo", "김포시/Gimpo",
                "남양주시/Namyangju", "동두천시/Dongducheon", "부천시/Bucheon", "성남시/Seongnam", "수원시/Suwon",
                "시흥시/Siheung", "안산시/Ansan", "안성시/Anseong", "안양시/Anyang", "양주시/Yangju",
                "양평군/Yangpyeong", "여주시/Yeoju", "연천군/Yeoncheon", "오산시/Osan", "용인시/Yongin", "의왕시/Uiwang",
                "의정부시/Uijeongbu", "이천시/Icheon", "파주시/Paju", "평택시/Pyeongtaek", "포천시/Pocheon", "하남시/Hanam",
                "화성시/Hwaseong"
                ]
        Combobox(self.MainFrame2, values=data, textvariable=self.local1, font=("휴먼매직체", 28), justify=RIGHT,
                 width=20).grid(row=0,column=0,sticky=N+W)


        self.graphFrame=Frame(self.MainFrame2)
        self.FrameName = Label(self.graphFrame, text=self.local1.get() + " 월별 지역화폐 카드 사용량 비교", bg='white',font=("휴먼매직체 28 bold"))
        self.FrameName.pack(side='top')
        self.graphFrame.grid(sticky=N+W,pady=10)
        self.graphCanvas=Canvas(self.graphFrame,width=1300,height=400,bg='white')
        self.graphCanvas.pack(pady=10)

        self.drawButton = Button(self.graphFrame, text="그래프 그리기", command=self.DrawGraph)
        self.drawButton.pack()







    def __init__(self):
        self.window=Tk()
        self.window.title("경기도지역화페 가맹점 검색")
        self.window.geometry("1400x680")
        self.window.configure(background='lightBlue')

        self.notebook = tkinter.ttk.Notebook(self.window, width=1400, height=680)
        self.notebook.pack()



        self.MainFrame1=Frame(self.window,background='lightBlue')
        self.notebook.add(self.MainFrame1, text="검색하기")
        #이미지 넣기
        photo=PhotoImage(file="Gmoney.png")
        imageLabel=Label(self.MainFrame1,image=photo,background='lightBlue')
        imageLabel.grid(row=0,column=1,pady=10,sticky=N+E+W)


        self.rLst=[] #검색결과 리스트

        self.selectResult=None #선택된 결과

        self.searchFrame=LabelFrame(self.MainFrame1)
        #self.searchFrame.grid(sticky=W+N,padx=5)
        self.searchFrame.grid(row=0,column=0,padx=5)
        Label(self.searchFrame,text="지역", font = ("휴먼매직체",30)).grid(row=0,column=1)
        Label(self.searchFrame,text="상호명", font = ("휴먼매직체",30)).grid(row=1,column=1)

        Label(self.searchFrame,text="도로명주소", font = ("휴먼매직체",30)).grid(row=2,column=1)
        Label(self.searchFrame,text="지번주소", font = ("휴먼매직체",30)).grid(row=3,column=1)
        Label(self.searchFrame,text="이메일", font = ("휴먼매직체",30)).grid(row=4,column=1)
        #self.local = StringVar() //함수로 잘되면 이부분 지우기
        #Entry(self.searchFrame, textvariable=self.local, font=("휴먼매직체", 30), justify=RIGHT, width=30).grid(row=0,column=2)
        self.InitCityNames()
        self.storeName = StringVar()
        Entry(self.searchFrame, textvariable=self.storeName, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=1, column=2)
        self.roadAddress = StringVar()  #도로명주소
        Entry(self.searchFrame, textvariable=self.roadAddress, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=2, column=2)
        self.localAddress = StringVar()  # 지번주소
        Entry(self.searchFrame, textvariable=self.localAddress, font=("휴먼매직체", 30), justify=RIGHT, width=30).grid(row=3,
                                                                                                             column=2)
        self.mailAdress = StringVar() #이거는 메일주소
        self.mailAdress.set("")
        Entry(self.searchFrame, textvariable=self.mailAdress, font=("휴먼매직체", 30), justify=RIGHT, width=30).grid(row=4,column=2)
        #self.futureValue = StringVar() //이거뭐야?
        #Label(self.searchFrame, textvariable=self.futureValue).grid(row=5, column=2, stick=E)

        Button(self.searchFrame, text="검색하기", font = ("휴먼매직체",20),command=self.search).grid(row=5, column=2, stick=E)

        #검색 결과  리스트박스 스크롤바가 있는 프레임
        self.InitTreeView()

        self.canvasFrame=Frame(self.MainFrame1,height=100)
        self.canvasFrame.grid(row=1,column=1,pady=5,padx=5,sticky=S+N)
        self.canvas=Canvas(self.canvasFrame,bg='white')
        Label(self.canvasFrame, text="가맹점 정보",font=("궁서체 15 bold")).pack(anchor='n')
        self.canvas.pack(anchor='center')

        self.mapButton=Button(self.canvasFrame,text="지도",command=self.SearchMap)
        self.mapButton['state']='disable'
        self.mapButton.pack(side=LEFT,padx=5)
        self.mailButton = Button(self.canvasFrame, text="메일 보내기", command=self.sendMail)
        self.mailButton['state'] = 'disable'
        self.mailButton.pack(side=LEFT,padx=5)

        self.MainFrame2=Frame(self.window,background='lightBlue')
        self.notebook.add(self.MainFrame2,text="도시별 월 사용 비교")
        self.InitGraph()



        self.window.mainloop()




MainGUI()
