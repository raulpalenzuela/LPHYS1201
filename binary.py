number = input("Enter a number: ")
rest = 0
binary = ""
while number != 0:
    rest = number % 2
    number = number // 2
    binary += str(rest)
print(binary[::-1]) 