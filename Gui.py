from tkinter import *

root = Tk()
root.title("Pines")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="정보")

menu.add_cascade(label="더보기", menu=menu_file)

root.config(menu=menu)

root.geometry("350x200")
root.resizable(False, False)

root.mainloop()