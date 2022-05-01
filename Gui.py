import tkinter.ttk as ttk
from tkinter import *

#이름 정의
root = Tk()
root.title("Pines")

#버튼 프레임
btn_frame = Frame(root)
btn_frame.pack(fill="x")

#버튼 1
btn_1 = Button(btn_frame, padx=5, pady=5,width=10, text="Pro")
btn_1.pack(side="left")

#버튼 2
btn_2 = Button(btn_frame, padx=5, pady=5, width=10, text="Home")
btn_2.pack(side="right")

#로그 프레임
log_frame = Frame(root)
log_frame.pack(fill="x")
scrollbar = Scrollbar(log_frame)
scrollbar.pack(side="right", fill="y")

#로그
log = Listbox(log_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
log.pack(side="left", fill="both", expand=True)
scrollbar.config(command=log.yview)

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