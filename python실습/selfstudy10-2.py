from tkinter import *
import random

btnList = [None] * 9
fnameList = [
    "cute1.gif", "cute2.gif", "cute3.gif", "cute4.gif",
    "cute5.gif", "cute6.gif", "cute7.gif", "cute8.gif", "cute9.gif"
]
photoList = [None] * 9

random.shuffle(fnameList)

window = Tk()
window.geometry("210x210")

for i in range(9):
    photoList[i] = PhotoImage(file="gif2/" + fnameList[i])  
    btnList[i] = Button(window, image=photoList[i])

num = 0
for i in range(3):
    for k in range(3):
        btnList[num].place(x=k*70, y=i*70)
        num += 1

window.mainloop()

#끝!
