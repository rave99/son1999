def get_fixed_price(discounted_price, discount_rate):
    # 할인율을 퍼센트로 받기 때문에 100에서 할인율을 뺀 후 나누어 정가 계산
    return discounted_price / ((100 - discount_rate) / 100)

def main():
    discount_rate = float(input("할인율은? "))
    price_a = float(input("A상품의할인된가격은? "))
    price_b = float(input("B상품의할인된가격은? "))

    fixed_price_a = get_fixed_price(price_a, discount_rate)
    fixed_price_b = get_fixed_price(price_b, discount_rate)

    print(f"A상품의정가는 {int(fixed_price_a)} 원")
    print(f"B상품의정가는 {int(fixed_price_b)} 원")

if __name__ == "__main__":
    main()
