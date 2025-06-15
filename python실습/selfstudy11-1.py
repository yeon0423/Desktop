inFp = None
inStr = ""

line_num = 0

inFp = open("data1.txt", "r")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    line_num += 1
    print("%d: %s" % (line_num, inStr.rstrip()))

inFp.close()