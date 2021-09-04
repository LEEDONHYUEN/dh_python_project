#
# # print("Hello world")
# #
# # # variable 변수
# # #a = 3
# # #a = 4
# #
# # #정수, int
# # #print(type(a))
# #
# # # str, 문자, "1233", '1233'
# # #a = 'wow'
# # #print(a, type(a))
# #
# # # 3.1 , 3.3 float
# # #a = 3.1
# # #print(a, type(a))
# #
# # # 사칙연산, +, -, *, /, %
# #
# # #a = 16%7
# # #print(a, type(a))
# #
# # # if 문
# #
# # #a = 3
# # # == (같다), != (다르다)
# # #if a != 5:
# #     #print('true')
# #
# # # 숫자를 입력 받을건데 이게 짝수면
# # # even 출력, 홀수면 odd 를 입력
# # # type change
# # #num = int(input())
# # #print(num)
# #
# # #num = int(input())
# # #a = num%2
# # #if a == 1:
# #     #print('odd')
# #
# # #else:
# #     #print('even')
# #
# # # elif는
# # # else는 elif 또는 if가 조건에 만족못하면 사용
# # # for 문 반복문
# # # i가 보통 변수라고함
# # # 소수 1과 자기 자신으로 나눠 떨어지느너
# # # inout으로 입력받고 소수면 prim, not prime
# # for i in range(11):
# #     print('*'*i)
# # for i in range(11):
# #     print('*'* (9-i))
# # # 소수 구하시오.
# #
# #
# #
# #
# # a=3
# # b=2
# #
# # if a==3 and b==2:
# #     print("Hi")
# # if a==3 or b!=2:
# #     print("ye")
# #
# # a = int(input("Enter the number"))
# # count = 0
# # for i in range (2,a):
# #     if a % i == 0:
# #         count +=1
# #
# # if count == 0:
# #     print("prime")
# # else:
# #     print("not prime")
# #
# # for i in range(13):
# #     if i==10:
# #         continue
# #         print(i)
#
# # b=[]
# # c=[1,2,3,4,5]
# #
# # b.append(1)
# # c.append(2)
# # import random
# #
# # a = random.randrange(1,100)
# # print(a)
#
# import random
# a=[]
# b = []
# a.append(1*10)
#
# for i in range(100):
#     a.append(i)
#
# for j in range(100):
#     c = random.randrange(1,100)
#     b.append(c)
#print(a,bssaaeeww)




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

# import random
# a=[]
# b = []
# a.append(1*10)
#
# for i in range(100):
#     a.append(i)
#
# for j in range(100):
#     c = random.randrange(1,100)
#     b.append(c)
# print(a,b)
#
# i=0
# #while i < 5:
#     #print("hi",i)
#     #i=i+1
# while i<100:
#
#     i=i+1
#     if i%3==0:
#         print("*")
#     elif i%3!=0:
#         print(i)
# i=0
# while i <11:
#     print("*"*(11-i))
#     i = i + 1
#
# for i in range(1,100):

        #3#one=i%10
       # ten=i//10
        #first_if=one!0 and ten !=0=and one% 3==0
        #second_if=ten %3==

#alist= []
#blist= []
#for i in range(5):
    #a = input("奈黨蘭刀渦 捕樓鬪渴 或銀 醱己曀 鞀偄 寅骨丹童 李持漫 葡螂堯意 對決")
    #b = input("浦浪基臺龍")
    #alist.append(a)
    #blist.append(b)
    #if a==b:
        #nonprint()

#print(alist, blist)

id_list = []
pwd_list = []
for i in range(5):
   temp_id=input("enter the your id : ")
   temp_pwd = input("enter the your pwd : ")
   count = 0
   for i in range(len(id_list)):
        if id_list[i] == temp_id:
            count = 1
        if count == 0:
            id_list.append(temp_id)
            print("not overlap")
        else:
            print("overlap")
   pwd_list.append(temp_pwd)
print(id_list)
print(pwd_list)
id_list = []
count = 0
temp_id=input()
# for i in range(len(id_list)):
#     if id_list[i] == temp_id:
#         count = 1
# if count == 0:
#     print("not overlap")
# else:
#     print("overlap")
#append= 리스트에 값을 집어넣는 것
#int(input("x"))
#문자 x를 숫자 x로 전환시켜주기 위해 int를 사용한다.
#로그인하는 코딩에서 중복값에 대해 코드화한다.
