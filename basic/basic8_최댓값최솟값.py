c = int(input())
d = list(map(int, input().split(' ')))


min_index = 0
max_index = 0

for i in range(len(d)):

    if d[min_index] > d[i]:
        min_index = i
    if d[max_index] < d[i]:
        max_index = i
