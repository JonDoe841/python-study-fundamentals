word=input()
counter=0
my_list=[]

for letter in word:
    if letter.isupper():
        upper_letter=letter
        curr_counter=counter
        my_list.append(curr_counter**1)
    counter += 1

print(my_list)