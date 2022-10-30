cards = [str(x) for x in input().split(", ")]
num_commands = int(input())
current_command = ""
current_card = ''
index = ""
for i in range(num_commands):
    commands = [str(x) for x in input().split(", ")]
    if len(commands) == 3:
        current_command, index, current_card = commands
    elif len(commands) == 2:
        current_command, current_card, = commands
    if current_command == "Add":
        if current_card not in cards:
            cards.append(current_card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    if current_command == "Remove":
        if current_card not in cards:
            print("Card not found")
        else:
            cards.remove(current_card)
            print("Card successfully removed")
    if current_command == "Remove At":
        index = current_card
        if int(index) > len(cards) or int(index) < 0:
            print("Index out of range")
        else:
            cards.pop(int(index))
            print("Card successfully removed")
    if current_command == "Insert":
        if int(index) > len(cards) or int(index) < 0:
            print("Index out of range")
        elif current_card in cards:
            print("Card is already added")
            continue
        else:
            cards.insert(int(index), current_card)
            print("Card successfully added")
last_cards = ", ".join(cards)
print(last_cards)