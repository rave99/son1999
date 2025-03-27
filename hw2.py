def get_integer(prompt):
    return int(input(prompt))

def exchange(amount):
    coins = [500, 100, 50, 10]  # 동전의 우선순위
    counts = {}  # 동전 개수를 저장할 딕셔너리
    
    for coin in coins:
        counts[coin] = amount // coin  # 해당 동전 개수 계산
        amount %= coin  # 남은 금액 갱신
    
    # 결과 출력
    for coin in coins:
        print(f"{coin}원 동전의 개수: {counts[coin]}")

# 사용자 입력 받기
amount = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(amount)
