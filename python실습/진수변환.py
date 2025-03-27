base = int(input("입력 진수 결정(16/10/8/2) : "))
value = input("값을 입력하세요 : ")

num = int(value, base)

print(f"16진수 ==> {hex(num)}")
print(f"10진수 ==> {num}")
print(f"8진수 ==> {oct(num)}")
print(f"2진수 ==> {bin(num)}")
