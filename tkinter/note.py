import os  # 파일 처리시 필요
from tkinter import *

root = Tk()
root.title("제목없음 - Window메모장")
root.geometry("640x480") #가로 세로, 소문자x 를 써야 됨. X,* 쓰면 오류남

#열기, 저장 파일 이름
filename = "mynote.txt"
def open_file():
    if os.path.isfile(filename): #있으면 True , 없으면 False
        with open(filename, "r" , encoding="utf-8") as file:
            txt.delete("1.0", END) #텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w" , encoding="utf-8") as file:
            file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

menuv = Menu(root) 

#파일 
#대메뉴>중메뉴 설정
menu_file = Menu(menuv, tearoff=0)
menu_file.add_command(label="열기" , command=open_file)
menu_file.add_command(label="저장" , command=save_file)
menu_file.add_separator() # 구분자
menu_file.add_command(label="끝내기" , command=root.quit)
menuv.add_cascade(label="파일", menu=menu_file) #대메뉴 명

menuv.add_cascade(label="편집") #대메뉴만
menuv.add_cascade(label="서식") #대메뉴만
menuv.add_cascade(label="보기") #대메뉴만
menuv.add_cascade(label="도움말") #대메뉴만

#스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right" , fill="y") #fill=y :  위아래로 꽉 채움

#본문 영역
txt = Text(root , yscrollcommand=scrollbar.set)
txt.pack(side="left" , fill="both" , expand=True)

scrollbar.config(command=txt.yview) #스크롤바에 리스트박스 매핑
root.config(menu=menuv)  # 14줄의 메뉴를 넣는다.

root.mainloop() # 창이 닫히지 않도록