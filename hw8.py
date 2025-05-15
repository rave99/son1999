# hw8.py

def buy(shopping_bag):
    print("[구입]")
    item = input("상품명? ")
    if item == "":
        return False
    qty = int(input("수량은? "))
    if item in shopping_bag:
        shopping_bag[item] += qty
    else:
        shopping_bag[item] = qty
    print(f"장바구니에 {item} {qty}개가 담겼습니다.\n")
    return True

def show(shopping_bag):
    print("\n>>> 장바구니 보기:", shopping_bag, "\n")

def find(shopping_bag):
    print("[검색]")
    item = input("장바구니에서 확인하고자 하는 상품은? ")
    if item in shopping_bag:
        print(f"{item}(는) {shopping_bag[item]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {item}(은)는 없습니다.")

# 주 프로그램부
shopping_bag = {}

while True:
    if not buy(shopping_bag):
        break

show(shopping_bag)
find(shopping_bag)
