import random
pr = [random.randrange(100),random.randrange(100),random.randrange(100),random.randrange(100),random.randrange(100)]
print(pr)
min_value = pr[0]
for t in range(len(pr)):
    min = t
    for i in range(len(pr)):
        if min_value > pr[i]:
            min_value = pr[i]
