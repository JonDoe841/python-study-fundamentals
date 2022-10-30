note_results = input()
my_list = note_results.split(" ")
players_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
players_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_terminated = False
for card in my_list:
    num = int(card[2:])
    if "A" in card:
        if num in players_A:
            players_A.remove(num)
    elif "B" in card:
        if num in players_B:
            players_B.remove(num)
    if len(players_A) < 7 or len(players_B) < 7:
        is_terminated = True
        break
print(f"Team A - {len(players_A)}; Team B - {len(players_B)} ")
if is_terminated:
    print("Game was terminated")
