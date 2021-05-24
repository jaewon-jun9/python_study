import tkinter.ttk as ttk  #콤보박스를 쓰려면 tkinter.ttk 를 추가 해야 한다. 

from tkinter import *




root = Tk()

root.title("파이썬 GUI")

root.geometry("640x480")

 

values = [str(i) + "일" for i in range(1,32)] #1~31까지의 숫자

combobox = ttk.Combobox(root, height=5, values=values)  # height=5 :목록 5개까지 보여줌

combobox.pack()

combobox.set("카드결제일") # 최초 목록 제목 설정

 

#읽기 전용 콤보박스 state="readonly"

readonly_combobox = ttk.Combobox(root, height=10, values=values , state="readonly")   #height=10 : 목록 10개까지 보여줌

readonly_combobox.current(0) # 0번째 index 값 선택

readonly_combobox.pack()


def btncmd():

    print(combobox.get()) #선택된 값 표시

    print(readonly_combobox.get()) #선택된 값 표시




btn = Button(root, text="선택" , command=btncmd)

btn.pack()


root.mainloop() 