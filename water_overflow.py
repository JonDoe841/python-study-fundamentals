num_lines = int(input())
tank_cap = 255
water_counter = 0
for current_line in range(num_lines):
    liters_of_water = int(input())
    if tank_cap - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    tank_cap -= liters_of_water
    water_counter += liters_of_water
print(water_counter)