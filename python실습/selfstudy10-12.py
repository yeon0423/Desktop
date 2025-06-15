from tkinter import *
from time import *

fnameList = ["ocean1.gif", "ocean2.gif", "ocean3.gif", "ocean4.gif", "ocean5.gif",
             "ocean6.gif", "ocean7.gif", "ocean8.gif", "ocean9.gif"]
num = 0

max_index = len(fnameList) - 1

def clickNext():
    global num
    num += 1
    if num > max_index:
        num = 0
    update_image_and_filename()

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = max_index
    update_image_and_filename()

def update_image_and_filename():
    global num
    photo = PhotoImage(file = "gif3/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    filenameLabel.configure(text=fnameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

filenameLabel = Label(window, text=fnameList[num], font=("", 10))

photo = PhotoImage(file = "gif3/" + fnameList[num])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
filenameLabel.place(x = 320, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()