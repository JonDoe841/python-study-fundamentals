num = int(input())
start_num = 0
final_num = 0
spec = ""
for i in range(0, num):
    start_num += 1
    if start_num > 10:
        my_list = [int(x) for x in str(start_num)]
        num_one = my_list[0]
        num_two = my_list[1]
        final_num = num_two + num_one

    if start_num == 5 or start_num == 7 or final_num == 5 or final_num == 7:
        spec = "True"
    else:
        spec = "False"
    print(f"{start_num} -> {spec}")
