strings = input()
splits = str.split(strings)
counter = len(strings.split())
sheep_counter = 0
warning_counter = 0


for split in splits:
    if counter == 1:
        if split == 'wolf':
            print(f'Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {warning_counter - 1}! You are about to be eaten by a wolf!')
    if split[:-1] == 'sheep' or split == 'sheep':
        sheep_counter += 1
    if split[:-1] == 'wolf' or split == 'wolf':
        warning_counter = counter
    counter -= 1
