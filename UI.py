from tkinter import *
from tkinter.ttk import Combobox
import Search
WIDTH=1200
HEIGHT=600
class MainGUI():
    def search(self):
        print(self.local.get())

        self.rLst=Search.search(self.local.get())
        self.changeSearchListbox()
    def changeSearchListbox(self):
        self.listBox.insert(0,"홍순조 천재")
        for i in range(len(self.rLst)):
            self.listBox.insert(i,self.rLst[i])



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
