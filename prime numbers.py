for i in range(1000):
    divisions = 0
    for j in range(i+1):
        if j == 0:
            continue
        
        if i%j == 0:
            divisions += 1
            
    if divisions == 2:
        print(i)