num_symbol = int(input())
for first_symbol in range(num_symbol):
    for second_symbol in range(num_symbol):
        for third_symbol in range(num_symbol):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")
            