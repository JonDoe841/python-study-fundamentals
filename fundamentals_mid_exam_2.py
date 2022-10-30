data = [str(x) for x in input().split(">>")]
final_tax = 0
for i in range(len(data)):
    current_vehicle = data[i]
    vehicle, year, distance = current_vehicle.split(" ")
    if vehicle == "family":
        tax = 50
        tax -= int(year) * 5
        tax += int(int(distance) / 3000) * 12
    elif vehicle == "heavyDuty":
        tax = 80
        tax -= int(year) * 8
        tax += int(int(distance) / 9000) * 14
    elif vehicle == "sports":
        tax = 100
        tax -= int(year) * 9
        tax += int(int(distance) / 2000) * 18
    else:
        print("Invalid car type.")
        continue
    print(f"A {vehicle} car will pay {tax:.2f} euros in taxes.")
    final_tax += tax
print(f"The National Revenue Agency will collect {final_tax:.2f} euros in taxes.")