print("사용할 진수를 선택하세요 (2, 8, 10, 16 증 하나)")
base = int(input("진수 입력:"))

number_str = input(f"{base} 진수 숫자 입력: ")

number = int(number_str, base)

print("\n변환 결과:")
print("2진수 :", bin(number)[2:])
print("8진수 :", oct(number)[2:])
print("10진수 :", number)
print("16진수 :", hex(number)[2:]).upper