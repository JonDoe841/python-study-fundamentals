divisor = int(input())
boundary = int(input())
num = 0
while True:
    if num > boundary:
        num -= divisor
        break
    num += divisor
print(num)