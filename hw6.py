# 구구단 전체 출력: 2~5단 4열, 줄바꿈 후 6~9단 4열

# 2단~5단 출력
for i in range(1, 10):
    for dan in range(2, 6):
        print(f"{dan} x {i} = {dan * i:2}", end="   ")
    print()

print()  # 한 줄 띄우기

# 6단~9단 출력
for i in range(1, 10):
    for dan in range(6, 10):
        print(f"{dan} x {i} = {dan * i:2}", end="   ")
    print()
