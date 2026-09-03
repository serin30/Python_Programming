#반복문 : while문 , for문

#while문
# 1~10까지의 반복 출력
i = 1
while i < 11:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
found = False

while i < len(nums):
    if nums[i] == target:
        print(f"{target} found")
        break
    i += 1
else:
    print(f"{target} not found")
# if not found:
#     print(f"{target} not found")

# 1~10 sum
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
else:
    print(f"sum : {tot}")

# 1~10 even num sum (way 1)
i = 1
tot = 0

while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1
else:
    print(f"sum : {tot}")

# 1~10 even num sum (way 2)
i = 1
tot = 0

while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += 1
else:
    print(f"sum : {tot}")
