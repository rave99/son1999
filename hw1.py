Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_radius(prompt):
...     r = int(input(prompt))
...     return r
... 
... def get_circle_area(radius):
...     return 3.14 * radius * radius
... 
... # 사용자 입력 받기
... radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
... 
... # 원의 넓이 계산
... area = get_circle_area(radius)
... 
... # 결과 출력
... print(f"반지름 {radius}인 원의 넓이 = 3.14 x {radius} x {radius} = {area}")
... 
SyntaxError: invalid syntax
>>> 
>>> 
=== RESTART: /Users/parkjaejung/Desktop/파이썬 프로그래밍 과제들/-/hw1.py ===
넓이를 구하고자 하는 원의 반지름은? 4
반지름 4인 원의 넓이 = 3.14 x 4 x 4 = 50.24
