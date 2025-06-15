inFp, outFp = None, None
inStr = ""

in_fname = input("소스 파일명을 입력하세요 : ")
out_fname = input("타겟 파일명을 입력하세요 : ")

try:
    inFp = open(in_fname, "r")
    outFp = open(out_fname, "w")

    inList = inFp.readlines()

    for inStr in inList:
        outFp.writelines(inStr)

    print(f"--- {in_fname} 파일이 {out_fname} 파일로 복사되었음 ---")

except FileNotFoundError:
    print("오류: 지정된 파일을 찾을 수 없습니다. 경로 또는 파일명을 확인해주세요.")
except Exception as e:
    print(f"파일 처리 중 오류 발생: {e}")

finally:
    if inFp:
        inFp.close()
    if outFp:
        outFp.close()