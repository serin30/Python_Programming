# 비트 연산자
a = 5  # 0000 0101
b = 3  # 0000 0011

print(a & b)  # 0000 0001
print(a | b)  # 0000 0111
print(a ^ b)  # 0000 0110
print(a << b)  # 5 -> 10 -> 20 -> 40
print(40 >> b)  # 40 -> 20 -> 10 -> 5
print(~a)  # 1111 0101 -> 0000 0101 -> 0000 0110 (-6)

#  멤버십 연산자
print("a" in "apple")

# 삼항 연산자 (int max = a > b ? a : b;)
max = a if a > b else b

# a가 짝수면 "짝수", 홀수면 "홀수"
print("홀수" if a % 2 else "짝수")

# 90점 이상이면 A
# 80점 이상이면 B
# 70점 이상이면 C
# 70점 미만이면 D
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(grade)
