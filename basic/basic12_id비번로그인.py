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
