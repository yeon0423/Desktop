from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event):
    # 일반 키 입력 처리 (Shift와 함께 눌리지 않은 경우)
    # print(f"일반 키 이벤트: {event.keycode}") # 디버깅용

    # Shift 키와 함께 화살표 키가 눌렸는지 확인
    if event.state & 0x0001:  # Shift 키가 눌린 상태 (0x0001은 Shift 키 상태 플래그)
        if event.keycode == 37: # 왼쪽 화살표
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")
        elif event.keycode == 38: # 위쪽 화살표
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")
        elif event.keycode == 39: # 오른쪽 화살표
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")
        elif event.keycode == 400: # 아래쪽 화살표 (힌트에서 400으로 주어짐)
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")
        # else:
        #     # Shift와 함께 다른 키가 눌렸을 때 (선택 사항)
        #     messagebox.showinfo("키보드 이벤트", f"눌린 키 : Shift + {chr(event.keycode)}")
    # Shift 키와 함께 눌리지 않은 다른 일반 키 처리 (선택 사항)
    # else:
    #     messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr(event.keycode))

## 메인 코드 부분 ##
window = Tk()
window.geometry("300x200") # 창 크기 임의 설정 (선택 사항)
window.title("키보드 이벤트 감지") # 창 제목 설정 (선택 사항)

# <Key> 이벤트 바인딩: 모든 키 입력을 keyEvent 함수로 보냅니다.
# keyEvent 함수 내에서 Shift 키 조합을 구분합니다.
window.bind("<Key>", keyEvent)

window.mainloop()