import math
radius = float(input("원의 반지름을 입력하세요: "))
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print(f"반지름이 {radius}인 원의 둘레는 {circumference:.2f}이고, 넓이는 {area:.2f}입니다.")