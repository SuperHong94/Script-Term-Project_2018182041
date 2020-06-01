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
        self.searchFrame.grid(row=1,column=1)
        Label(self.searchFrame,text="지역", font = ("휴먼매직체",30)).grid(row=1,column=1)
        Label(self.searchFrame,text="업종").grid(row=2,column=1)
        Label(self.searchFrame,text="도로명주소/지번주소").grid(row=3,column=1)
        self.money = StringVar()
        Entry(self.searchFrame, textvariable=self.money, justify=RIGHT,width=100).grid(row=1, column=2)
        self.years = StringVar()
        Entry(self.searchFrame, textvariable=self.years, justify=RIGHT).grid(row=2, column=2)
        self.rate = StringVar()
        Entry(self.searchFrame, textvariable=self.rate, justify=RIGHT).grid(row=3, column=2)
        self.futureValue = StringVar()
        Label(self.searchFrame, textvariable=self.futureValue).grid(row=4, column=2, stick=E)

        Button(self.searchFrame, text="검색하기", command=self.search).grid(row=5, column=2, stick=E)



        self.window.mainloop()




MainGUI()
