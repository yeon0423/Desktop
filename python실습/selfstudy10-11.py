from tkinter import *
import random

# 전역 변수 선언
btnList = [None] * 9
fnameList = [
    "cute1.gif", "cute2.gif", "cute3.gif", "cute4.gif",
    "cute5.gif", "cute6.gif", "cute7.gif", "cute8.gif", "cute9.gif"
]
photoList = [None] * 9

# 이미지 파일 리스트를 임의로 섞기
random.shuffle(fnameList)

window = Tk()
window.geometry("210x210")

# PhotoImage 객체 생성 및 버튼에 이미지 넣기
for i in range(9):
    photoList[i] = PhotoImage(file="gif2/" + fnameList[i])  # 여기서 gif2로 경로 변경!
    btnList[i] = Button(window, image=photoList[i])

num = 0
for i in range(3):
    for k in range(3):
        btnList[num].place(x=k*70, y=i*70)
        num += 1

window.mainloop()
