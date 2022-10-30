days = int(input())
num_players = int(input())
group_energy = float(input())
water = (float(input()) * days) * num_players
food = (float(input()) * days) * num_players
for i in range(1, days + 1):
    current_day = i
    energy_lost = float(input())
    group_energy -= energy_lost
    if group_energy <= 0:
        break
    if current_day % 2 == 0:
        group_energy += group_energy * 0.05
        water *= 0.7
    if current_day % 3 == 0:
        group_energy += group_energy * 0.10
        food -= (food / num_players)
if group_energy <= 0:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")