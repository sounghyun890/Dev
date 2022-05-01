import tkinter.ttk as ttk
from tkinter import *

root = Tk()

#창 이름 정의
root.title("Pines")

#버튼 프레임
btn_frame = Frame(root)
btn_frame.pack()

#버튼 1
btn_1 = Button(root, text="Pro")
btn_1.pack(side="left")
#버튼 2
btn_2 = Button(root, text="Home")
btn_2.pack(side="right")

#진행상황 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x")

#진행상황
p_var = DoubleVar()
progress_var = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_var.pack(fill="x")

#사이즈 정의
root.geometry("350x200")
root.resizable(False, False)

root.mainloop()