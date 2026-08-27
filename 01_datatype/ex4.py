# 문자열
# "", ''
a = 'python'
print(a, type(a))

# I'll be back
print("I'll be back")
print('I\'ll be back')

multiline = """
Life is short
You need Python
"""
print(multiline)

# docstring


def func():
    """이 함수는 트세트용입니다."""
    pass


print(func.__doc__)

# 문자열 연결
print("Hello" + "Python")
# 문자열 반복
print("Hello" * 10)
print("*" * 50)

# 문자열끼리만 + 가능
# print("Hello" + str(10))
print("Hello" + str(10))

print("10" + "2")
print(int("10") + int("2"))

#문자열 포맷팅(f-string)
name = "pororo"
age = 23
print(f"이름: {name}, 나이: {age}살")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.1415

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789

print(f"{num:,}")
print(f"{num:15d}")
print(f"{num:015,d}")
