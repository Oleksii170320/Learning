temperatures = [73,74,75,71,69,72,76,73]

res = []

if len(temperatures) == 0:
    res.append(0)
elif len(temperatures) > 0:
    c = 0
    for i in range(len(temperatures) - 1):
        for t in range(i+1, len(temperatures)):
            t1 = temperatures[i]
            t2 = temperatures[t]
            if temperatures[i] <= temperatures[t]:
                c += 1
                res.append(c)
                break
            elif temperatures[i] > temperatures[t]:
                c += 1
                if len(temperatures) - i == 2:
                    res.append(0)

        c = 0
    res.append(0)



print(res)