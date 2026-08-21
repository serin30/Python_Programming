# 변수 
a = 2
b = 3
print(a, end="")
print(b)
print(a, b, sep=",")

a = 2; b = 3
print(a, b) 

a, b = (2, 3) # 튜플 언패킹
print(a, b)

a = b = c = 0

# 값 swap
a, b = 2, 3
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어 사용 불가
# snake_case
# camelCase

# 2name = "pororo"
# name! = "pororo"
# class = "test"

이름 = "뽀로로"
print(이름)
