string = "   h  ey wh    . ats.u, j   'ai 3    "
separators = [" ", ",", ".", "'"]
words = 0
in_word = False

for l in string:
    if l not in separators:
        if in_word == False:
            words += 1
        in_word = True
    else:
        in_word = False
print(words)