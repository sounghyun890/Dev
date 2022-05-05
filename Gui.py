import tkinter.ttk as ttk
from tkinter import *
import os

#이름 정의
root = Tk()
root.title("Pines")

#버튼 프레임
btn_frame = Frame(root)
btn_frame.pack(fill="x")

#버튼 1
def btn1():
    os.system('slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
    os.system('slmgr /skms kms8.msguides.com')
    os.system('slmgr /ato')
btn_1 = Button(btn_frame, padx=5, pady=5,width=10, command=btn1, text="Pro")
btn_1.pack(side="left")

#버튼 2
def btn2():
    os.system('slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
    os.system('slmgr /skms kms8.msguides.com')
    os.system('slmgr /ato')
btn_2 = Button(btn_frame, padx=5, pady=5, width=10, command=btn2, text="Home")
btn_2.pack(side="right")

#사이즈 정의
root.geometry("300x50")
root.resizable(False, False)
root.mainloop()
