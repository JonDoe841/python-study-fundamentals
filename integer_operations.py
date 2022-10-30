num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())


def math(num1, num2, num3, num4, *final_math):
     final_math = ((num1 + num2) // num3) * num4
     return final_math

print(f"{math(num1, num2, num3, num4):.0f}")