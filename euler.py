e = 1
i = 1
fact_index = 1
while i <= 10**9:
    e += 1/i
    fact_index += 1
    i *= fact_index
print(e)