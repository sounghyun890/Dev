from tkinter import *

#안녕

root = Tk()
root.title("Pines")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="정보")

root.config(menu=menu)

root.geometry("250x100")
root.resizable(False, False)

root.mainloop()