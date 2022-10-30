strings = input()
counter = 0
strings = strings.casefold()

if strings.find('Sand'.casefold()) >= 0:
    counter += 1
if strings.find('Water'.casefold()) >= 0:
    counter += 1
if strings.find('Fish'.casefold()) >= 0:
    counter += 1
if strings.find('Sun'.casefold()) >= 0:
    counter += 1

print(counter)
