inFp = None
inStr = ""

line_num = 0

# data1.txt가 파이썬 스크립트와 같은 폴더에 있다고 가정
inFp = open("data1.txt", "r")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    line_num += 1
    print("%d: %s" % (line_num, inStr.rstrip())) # rstrip()으로 불필요한 개행문자 제거

inFp.close()