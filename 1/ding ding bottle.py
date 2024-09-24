for i in range(100):
    five = False
    seven = False
    if i % 5 == 0 and i%7 == 0:
        print("ding ding bottle")
    elif i % 5 == 0:
        print("ding ding")
    elif i % 7 == 0:
        print("bottle")
    else:
        print(i)