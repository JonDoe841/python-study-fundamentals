num_ppl = int(input())
num_capacity = int(input())
num_courses = num_ppl // num_capacity
if num_ppl % num_capacity != 0:
    num_courses += 1
print(num_courses)