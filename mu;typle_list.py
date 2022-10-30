num = int(input())
limit = int(input())
my_list = []
math = 0
for i in range(limit):
    math += num
    my_list.append(math)
print(my_list)