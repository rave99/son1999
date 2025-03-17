def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    return 3.14 * radius * radius

# 사용자 입력 받기
radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")

# 원의 넓이 계산
area = get_circle_area(radius)

# 결과 출력
print(f"반지름 {radius}인 원의 넓이 = 3.14 x {radius} x {radius} = {area}")
