from tkinter import *
from time import *

## 전역 변수 선언 부분 ##
# 이미지 파일 리스트를 9개의 ocean 이미지로 설정합니다.
fnameList = ["ocean1.gif", "ocean2.gif", "ocean3.gif", "ocean4.gif", "ocean5.gif",
             "ocean6.gif", "ocean7.gif", "ocean8.gif", "ocean9.gif"]
num = 0

# 리스트의 마지막 인덱스를 동적으로 계산합니다. (9개 이미지이므로 max_index는 8이 됩니다.)
max_index = len(fnameList) - 1

## 함수 선언 부분 ##
def clickNext():
    global num
    num += 1
    if num > max_index: # 리스트의 마지막을 넘어가면
        num = 0 # 처음으로 돌아감
    update_image_and_filename()

def clickPrev():
    global num
    num -= 1
    if num < 0: # 리스트의 처음보다 작아지면
        num = max_index # 마지막으로 돌아감
    update_image_and_filename()

def update_image_and_filename():
    """현재 이미지와 파일명 레이블을 업데이트하는 헬퍼 함수"""
    global num
    # 이미지 파일 경로에서 폴더 이름은 'gif3'으로 유지합니다.
    photo = PhotoImage(file = "gif3/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo  # 가비지 컬렉션 방지
    filenameLabel.configure(text=fnameList[num]) # 파일명 레이블 업데이트

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

# 파일명 표시를 위한 레이블 추가 (초기 파일명 설정)
filenameLabel = Label(window, text=fnameList[num], font=("", 10))

# 초기 이미지 설정 (이미지 파일 경로에서 폴더 이름을 'gif3'으로 유지합니다.)
photo = PhotoImage(file = "gif3/" + fnameList[num])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
filenameLabel.place(x = 320, y = 10) # 버튼 사이에 위치 조정 (x 값은 적절히 조절)
pLabel.place(x = 15, y = 50)

window.mainloop()