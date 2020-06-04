from tkinter import *


class MainGUI():
    startRow=1
    def search(self):
        pass
    def __init__(self):
        self.window=Tk()
        self.window.title("경기도지역화페 가맹점 검색")
        self.window.geometry("1200x600")
        self.searchFrame=Frame(self.window)
        self.searchFrame.grid(row=0,column=0)
        Label(self.searchFrame,text="지역", font = ("휴먼매직체",30)).grid(row=0,column=1)
        Label(self.searchFrame,text="상호명", font = ("휴먼매직체",30)).grid(row=1,column=1)
        Label(self.searchFrame,text="업종", font = ("휴먼매직체",30)).grid(row=2,column=1)
        Label(self.searchFrame,text="도로명주소/지번주소", font = ("휴먼매직체",30)).grid(row=3,column=1)
        self.local = StringVar()
        Entry(self.searchFrame, textvariable=self.local, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=0, column=2)
        self.storeName = StringVar()
        Entry(self.searchFrame, textvariable=self.storeName, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=1, column=2)
        self.valueType = StringVar()
        Entry(self.searchFrame, textvariable=self.valueType, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=2, column=2)
        self.address = StringVar()
        Entry(self.searchFrame, textvariable=self.address, font = ("휴먼매직체",30), justify=RIGHT,width=30).grid(row=3, column=2)
        self.futureValue = StringVar()
        Label(self.searchFrame, textvariable=self.futureValue).grid(row=4, column=2, stick=E)

        Button(self.searchFrame, text="검색하기", font = ("휴먼매직체",20),command=self.search).grid(row=5, column=2, stick=E)

        self.resultFrame=Frame(self.window,bg="white")
        self.resultFrame.grid(row=1,column=0)
        listBox=Listbox(self.resultFrame,selectmode="extended")
        listBox.insert(0,"국어")
        listBox.pack(side=LEFT)

        self.window.mainloop()




MainGUI()
