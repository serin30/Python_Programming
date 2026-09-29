# 함수 2

# ===========================================================
# 1. 지역변수와 전역변수
# ===========================================================
# 함수 안에서 만든 변수는 지역변수로, 함수 밖에서는 사용할 수 없다.
# 함수 밖에서 선언된 변수는 전역변수이며, 함수 안에서는 기본적으로
# "읽기"만 가능하고, 값을 바꾸려면 global 키워드가 필요하다.

import time

from altair import value
a = 10  # 전역변수


def func():
    global a  # 전역변수 a를 사용하겠다고 명시
    a = 10   # 지역변수 -> 전역변수
    print("함수 안:", a)


func()
print("함수 밖:", a)

# ===========================================================
#  2. 함수 인자 전달 방식
# ===========================================================
# 1) call-by-value: 값 자체가 복사되어 전달, 원본과 별도의 메모리 공간을 할당, 함수 내부에서 수정 시 원본 불변 (IN C LANGUAGE TOO)
# 2) call-by-reference: 변수의 주소가 전달, 원본과 같은 메모리 공간을 가리킴, 함수 내부에서 수정 시 원본 변경 (IN C LANGUAGE TOO)
# 3) call-by-assignment: 파이썬은 객체를 가리키는 참조 전달, 원본과 같은 객체를 가리킴(재할당 전까지)
#                        immutable 객체인 경우 call-by-value처럼 동작 -> 함수 내부에서 수정 시 원본 불변
#                        mutable 객체인 경우 call-by-reference처럼 동작 -> 함수 내부에서 수정 시 원본 변경
#                        mutable 객체라도 재할당을 하면 원본과 연결이 끊기고 새로운 객체 할당


def swap(a, b):     # 매개변수 a, b는 함수 호출 시 전달된 객체의 참조값을 받음
    a, b = b, a
    print(a, b)  # 2, 1


a, b = 1, 2
print(id(a), id(b))  # a, b 객체의 참조값 전달
swap(a, b)    # a, b 객체의 참조값 전달
print(a, b)   # 1, 2


def append_item(num):
    num.append(2)


num = [1]
append_item(num)  # num 객체의 참조값 전달
print(num)       # [1, 2] -> 함수 내부에서 num 객체를 수정


def swap2(num):
    num[0], num[1] = num[1], num[0]


swap2(num)
print(num)


def assign(num):
    num = [10]
    print(num)


assign(num)  # [2, 1] -> 함수 내부에서 num 객체를 재할당
print(num)


# ===========================================================
# 3. 재귀함수
# ===========================================================

# 팩토리얼 계산하기 (1, 1, 2, 6, 24, ..)
# 점화식
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial(5)  # 5 * 4 * 3 * 2 * 1 = 120
print(factorial(5))  # ✅ 120

# 피보나치 계산하기 (0, 1, 1, 2, 3, 5, 8, ..)
# 점화식: F(n) = F(n-1) + F(n-2)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print([fibonacci(i) for i in range(11)])  # [0, 1, 1, 2, 3, 5, 8, ...]

# ===========================================================
# 4. 람다함수
# ===========================================================

# 람다함수 : 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda a, b, ...: 표현식


def add(a, b): return a + b


print(add)
print(add(3, 4))


students = [
    {"name": "뽀로로", "score": 85},
    {"name": "크롱", "score": 92},
    {"name": "포비", "score": 78},
]

# 이름 순으로 정렬
print(sorted(students, key=lambda s: s["name"]))

# 점수 순으로 정렬
print(sorted(students, key=lambda s: s["score"]))

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ n이 짝수면 True, 홀수면 False를 반환하는 함수 작성하기


def is_even(n):
    return n % 2 == 0


print(is_even(4))                           # ✅ True
print(is_even(7))                           # ✅ False


# 2️⃣ 가변 인자로 여러 숫자를 받아 (최소값, 최대값, 합계, 평균) 튜플 리턴하기

def num_info(*args):
    minimum = min(args)
    maximum = max(args)
    total = sum(args)
    average = total / len(args)
    return (minimum, maximum, total, average)


print(num_info(4, 8, 1, 9, 3))              # ✅ (1, 9, 25, 5.0)


# 3️⃣ 이름과 키워드 가변 인자로 받은 정보로 아래와 같이 문자열을 만들어 리턴하기

def introduce(name, **kwargs):
    info = [f"{k}: {v}" for k, v in kwargs.items()]
    return " / ".join([name] + info)


print(introduce("카리나", age=26, team="에스파", hometown="수원"))
# ✅ 카리나 / age: 26 / team: 에스파 / hometown: 수원

print(introduce("장원영", age=22, team="아이브", bloodtype="O형"))
# ✅ 장원영 / age: 22 / team: 아이브 / bloodtype: O형

print(introduce("성현", age=17, team="코르티스"))
# ✅ 성현 / age: 17 / team: 코르티스


# 4️⃣ 5부터 카운트다운하여 로켓 발사시키기 (재귀함수)
# time.sleep(1)                     # 1초 동안 stop
def countdown(n):
    if n == 0:
        print("로켓 발사")
    else:
        print(n, end=" -> ")
        time.sleep(1)
        countdown(n - 1)


countdown(5)                        # ✅ 5 -> 4 -> 3 -> 2 -> 1 -> 로켓 발사
