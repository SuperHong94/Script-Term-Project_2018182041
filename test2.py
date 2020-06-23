from tkinter import *
import tkinter.ttk
window=Tk()
window.title("경기도지역화페 가맹점 검색")
window.configure(background='lightBlue')


notebook=tkinter.ttk.Notebook(window, width=800, height=600)
notebook.pack()



frame1=Frame(window)
notebook.add(frame1, text="페이지1")
photo=PhotoImage(file="Gmoney.png")
imageLabel=Label(frame1,image=photo,background='lightBlue')
imageLabel.grid(row=0,column=1,pady=10,sticky=N+E+W)


frame2=Frame(window)
notebook.add(frame2, text="페이지2")

label2=Label(frame2, text="페이지2의 내용", fg='blue', font='helvetica 48')
label2.pack()

frame3=Frame(window)
notebook.add(frame3, text="페이지3")

label3=Label(frame3, text="페이지3의 내용", fg='green', font='helvetica 48')
label3.pack()

frame4=Frame(window)
notebook.insert(2, frame4, text="페이지4")

label4=Label(frame4, text="페이지4의 내용", fg='yellow', font='helvetica 48')
label4.pack()

window.mainloop()