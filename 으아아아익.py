c = int(input())
d = list(map(int, input().split(' ')))

count = 0

for i in range(len(d)):
    elm = d[i]
    flag = 1
    for k in range(1, elm//2 + 1):
        if elm % k == 0:
            flag += 1 #flag = flag + 1
            if flag >= 3:
                break
    if flag ==2:
        count += 1 #count = count + 1

print(count)



min_index = 0
max_index = 0

for i in range(len(d)):

    if d[min_index] > d[i]:
        min_index = i
    if d[max_index] < d[i]:
        max_index = i