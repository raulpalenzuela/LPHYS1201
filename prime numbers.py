for i in range(1000):
    divisions = 0
    
    for j in range(2, i+1): #1 is always a divisor
        if i%j == 0:
            divisions += 1
            
    if divisions == 1:
        print(i)