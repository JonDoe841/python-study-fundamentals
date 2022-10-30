num = [int(item) for item in input().split()]
for number in range(len(num)):
    real_num = num[number] * -1
    num[number] = real_num
print(num)
