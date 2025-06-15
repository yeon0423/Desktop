outFp = None
outStr = ""

# 사용자로부터 파일명을 입력받음
# 힌트: "폴더도 함께 입력 가능"
out_fname = input("파일명을 입력하세요 (예: data2.txt 또는 C:/Temp/data2.txt) : ")

# 입력받은 파일명으로 파일을 쓰기 모드("w")로 엽니다.
# 사용자가 존재하지 않는 폴더를 입력하면 오류가 발생할 수 있습니다.
outFp = open(out_fname, "w")

while True :
    outStr = input("내용 입력 : ")
    if outStr != "" :
        # writelines()는 리스트를 인자로 받지만, 단일 문자열도 작동합니다.
        # 하지만 명확성을 위해 write()를 사용하는 것이 더 좋습니다.
        # print()와는 달리, write()는 자동으로 줄바꿈을 해주지 않으므로 직접 '\n'을 추가합니다.
        outFp.write(outStr + "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")