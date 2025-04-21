import string
digits = "2337"


def alphaNums():
    alpha = string.ascii_lowercase
    d = {}
    c = 0

    for i in range(10):
        if i in (0, 1):
            continue
        else:
            world = str()
            if i in (7, 9):
                for j in range(c, c + 4):
                    world += alpha[j]
                    c += 1
            else:
                for j in range(c, c + 3):
                    world += alpha[j]
                    c += 1
            d[i] = world
    return d

a = alphaNums()

lett_list = []
rlist=[]

for i in digits:
    lett_list.append(a[int(i)])

if len(digits) == 0:
    print("[]")
elif len(digits) == 1:
    print(list(a[int(digits)]))
elif len(digits) == 2:
    k = lett_list[0]
    m = lett_list[1]
    for i in range(len(k)):
        for j in range(len(m)):
            rlist.append(f"{k[i]}{m[j]}")
elif len(digits)==3:
    k=lett_list[0]
    m=lett_list[1]
    l=lett_list[2]
    for i in range(len(k)):
        for j in range(len(m)):
            for p in range(len(l)):
                rlist.append(f"{k[i]}{m[j]}{l[p]}")
elif len(digits)==4:
    k=lett_list[0]
    m=lett_list[1]
    l=lett_list[2]
    f=lett_list[3]
    for i in range(len(k)):
        for j in range(len(m)):
            for p in range(len(l)):
                for g in range(len(f)):
                    rlist.append(f"{k[i]}{m[j]}{l[p]}{f[g]}")

print(rlist)
