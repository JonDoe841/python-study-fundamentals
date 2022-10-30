event = input()
coffee = 0
event_lower = ['coding', 'movie', 'dog', 'cat']
event_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']
while event != "END":
    if event in event_lower:
        coffee += 1
    elif event in event_upper:
        coffee += 2
    event = input()
    if event == "END":
        if coffee > 5:
            print("You need extra sleep")
        else:
            print(coffee)