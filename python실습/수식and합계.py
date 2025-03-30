a = int(input("'1.입력한 수식 계산, 2. 두 수 사이의 합계'를 선택하세요."))

if a == 1:
    k = input("수식을 입력하세요.")
    result = eval(k)
    print(f"'{k}'의 결과는 {result}입니다.")  # 추가된 부분

else:
    b = int(input("첫 번째 수를 입력하세요."))
    c = int(input("두 번째 수를 입력하세요."))
    
    result=b+c
    
    print(f"{b}+{c}는 {result}입니다.")
