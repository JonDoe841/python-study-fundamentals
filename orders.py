num_orders = int(input())
total_price = 0
for i in range(num_orders):
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())
    price = (capsule_price * capsule_per_day) * days
    if price == 0:
        pass
    else:
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")