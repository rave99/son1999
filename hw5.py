
def read_single_digit(num):
    korean_digits = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return korean_digits[num]

def read_number(num):
    # num은 항상 0~999 범위의 정수라고 가정
    result = ""
    if num < 10:
        result = read_single_digit(num)
    elif num < 100:
        tens = num // 10
        ones = num % 10
        result = read_single_digit(tens) + " " + read_single_digit(ones)
    else:
        hundreds = num // 100
        tens = (num % 100) // 10
        ones = num % 10
        result = read_single_digit(hundreds) + " " + read_single_digit(tens) + " " + read_single_digit(ones)
    print(result)

# 주 프로그램부
num = int(input("세 자리 정수 입력: "))
read_number(num)
