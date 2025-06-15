from tkinter import *
from tkinter import messagebox

def shift_arrow_left_pressed(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")

def shift_arrow_up_pressed(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")

def shift_arrow_right_pressed(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")

def shift_arrow_down_pressed(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")

window = Tk()
window.geometry("300x200")
window.title("키보드 이벤트 감지")

window.bind("<Shift-Left>", shift_arrow_left_pressed)
window.bind("<Shift-Up>", shift_arrow_up_pressed)
window.bind("<Shift-Right>", shift_arrow_right_pressed)
window.bind("<Shift-Down>", shift_arrow_down_pressed) 

window.mainloop()