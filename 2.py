import random as rand
n = 100000000
cnt = 0
for i in range(n):
    b = rand.random() * 4 - 2
    c = rand.random() * 4 - 2
    if b**2-4*c < 0:
        cnt+=1
print(cnt/n)
