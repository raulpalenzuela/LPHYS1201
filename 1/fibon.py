fibonacci = [1, 1]
for n in range(18):
	fibonacci.append(fibonacci[n] + fibonacci[n+1])
print(fibonacci)