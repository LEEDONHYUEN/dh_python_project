# A = int(input())
# B = int(input())
# C = int(input())
#
# d = A*B*C
#
# d = str(d)
# lililist = []
# for i in range(len(d)):
#     print(d[i])
#     lililist.append(d[i])
# print(lililist)


a = '555'
b = '666'
def find_max(c):

    temp = []
    for i in range(len(c)):
        if c[i] == "5":
            temp += "6"
        else:
            temp += c[i]

    return temp

max_a = find_max(a)
max_b = find_max(b)


M=51
N=100
def find_prime(a):
    count = 0
    for i in range(2, a//2 + 1):
        if a % i == 0:
            count += 1
            break
    if (count == 0 or a ==2) and a !=1 :
        return 1
    else:
        return 0
total_sum = 0
first_prime = 0

for i in range(n, m +1):
    flag = find_prime(i)
    if flag == 1:
        total_sum += i
        if first_prime == 0:
            first_prime = i
if first_prime == 0
    print("-1")
















