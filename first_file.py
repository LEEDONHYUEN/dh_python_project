# print("Hello world")
#
# # variable 변수
# #a = 3
# #a = 4
#
# #정수, int
# #print(type(a))
#
# # str, 문자, "1233", '1233'
# #a = 'wow'
# #print(a, type(a))
#
# # 3.1 , 3.3 float
# #a = 3.1
# #print(a, type(a))
#
# # 사칙연산, +, -, *, /, %
#
# #a = 16%7
# #print(a, type(a))
#
# # if 문
#
# #a = 3
# # == (같다), != (다르다)
# #if a != 5:
#     #print('true')
#
# # 숫자를 입력 받을건데 이게 짝수면
# # even 출력, 홀수면 odd 를 입력
# # type change
# #num = int(input())
# #print(num)
#
# #num = int(input())
# #a = num%2
# #if a == 1:
#     #print('odd')
#
# #else:
#     #print('even')
#
# # elif는
# # else는 elif 또는 if가 조건에 만족못하면 사용
# # for 문 반복문
# # i가 보통 변수라고함
# # 소수 1과 자기 자신으로 나눠 떨어지느너
# # inout으로 입력받고 소수면 prim, not prime
# for i in range(11):
#     print('*'*i)
# for i in range(11):
#     print('*'* (9-i))
# # 소수 구하시오.
#
#
#
#
# a=3
# b=2
#
# if a==3 and b==2:
#     print("Hi")
# if a==3 or b!=2:
#     print("ye")
#
# a = int(input("Enter the number"))
# count = 0
# for i in range (2,a):
#     if a % i == 0:
#         count +=1
#
# if count == 0:
#     print("prime")
# else:
#     print("not prime")
#
# for i in range(13):
#     if i==10:
#         continue
#         print(i)

# b=[]
# c=[1,2,3,4,5]
#
# b.append(1)
# c.append(2)
# import random
#
# a = random.randrange(1,100)
# print(a)

import random
a=[]
b = []
a.append(1*10)

for i in range(100):
    a.append(i)

for j in range(100):
    c = random.randrange(1,100)
    b.append(c)
print(a,bssaaeeww)




#     print("prime")
# else:
#     print("not prime")
#
# for i in range(13):
#     if i==10:
#         continue
#         print(i)

# b=[]
# c=[1,2,3,4,5]
#
# b.append(1)
# c.append(2)
# import random
#
# a = random.randrange(1,100)
# print(a)

import random
a=[]
b = []
a.append(1*10)

for i in range(100):
    a.append(i)

for j in range(100):
    c = random.randrange(1,100)
    b.append(c)
print(a,b)

i=0
#while i < 5:
    #print("hi",i)
    #i=i+1
while i<100:

    i=i+1
    if i%3==0:
        print("*")
    elif i%3!=0:
        print(i)
i=0
while i <11:
    print("*"*(11-i))
    i = i + 1

for i in range(1,100):

        one=i%10
        ten=i//10
        first_if=one!0 and ten !=0=and one% 3==0
        second_if=ten %3==
