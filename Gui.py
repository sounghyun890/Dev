import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Pines")

#버튼 프레임
btn_frame = Frame(root)
btn_frame.pack(fill="x")

#버튼 1
btn_1 = Button(root, padx=5, pady=5,width=10, text="Pro")
btn_1.pack(side="left")
#버튼 2
btn_2 = Button(root, padx=5, pady=5, width=10, text="Home")
btn_2.pack(side="right")

#진행상황 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x")

#진행상황
p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")

#사이즈 정의
root.resizable(False, False)

root.mainloop()