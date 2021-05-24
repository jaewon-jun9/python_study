import tkinter.ttk as ttk 
from tkinter import *




root = Tk()

root.title("파이썬 GUI")

root.geometry("640x480")

 

progressbar = ttk.Progressbar(root, maximum = 100 , mode = "indeterminate") # mode = "indeterminate" 결정되지 않음. 언제끝날지 모른다

progressbar = ttk.Progressbar(root, maximum = 100 , mode = "determinate") # mode = "determinate" 처음 부터 끝까지 

progressbar.start(10) #10ms 마다 움직임

progressbar.pack()

 

def btncmd():

    progressbar.stop() #작동 중지




btn = Button(root, text="중지" , command=btncmd)

btn.pack()




root.mainloop() 