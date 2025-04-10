for dan in range(2, 10):
    print(f"# {dan}단 #", end="   ")  
print()  

# 본문 출력
for i in range(1, 10):
    for dan in range(2, 10):
        print(f"# {dan} * {i} = {dan*i:>2} #", end="   ")  # 수식 출력
    print()  