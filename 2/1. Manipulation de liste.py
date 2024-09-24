i = 0
number_list = []
while i < 5:
    input_number = int(input(f"{i+1}. Input a number between 1 and 20: "))
    if input_number < 1 or input_number > 20:
        continue
    number_list.append(input_number)
    i += 1

print(number_list)

for number in number_list:
    if number % 2 == 0:
        number_list.remove(number)

print(number_list)