c = 0
s = 0
for i in range(1,98):
    for j in range(1,98):
        for k in range(1,98):
            if i != j and i != k and j != k:
                c += 1
                l = sorted([i,j,k])
                if l[2] - l[1] == l[1] - l[0]:
                    s += 1
print(s/c)
