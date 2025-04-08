l = [1,0,0,0,1]

for i, f in enumerate(l):
    if f == 0 and (l[i - 1] == 0 and l[i + 1] == 0 ):
        l[i] = 1

print(l)