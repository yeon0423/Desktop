outFp = None
outStr = ""

out_fname = input("파일명을 입력하세요 (예: data2.txt 또는 C:/Temp/data2.txt) : ")

outFp = open(out_fname, "w")

while True :
    outStr = input("내용 입력 : ")
    
    if outStr != "" :
        outFp.write(outStr + "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")