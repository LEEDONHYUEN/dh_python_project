
def make_map():

    tic_map = [" " for i in range(9)]
    '''
    tic_map = []
    for i in range(9):
        tic_map.append(0)
    '''

    return tic_map
aser=make_map()

def print_map(tic_map):
    print("-------")
    print(tic_map[0]+"ㅣ"+tic_map[1]+"ㅣ"+tic_map[2])
    print("-------")
    print(tic_map[3]+"ㅣ"+tic_map[4]+"ㅣ"+tic_map[5])
    print("-------")
    print(tic_map[6]+"ㅣ"+tic_map[7]+"ㅣ"+tic_map[8])


def put_abatar(tic_map):
     while True:
         pos= int(input("Enter your ldcation : "))
         if tic_map[pos] == " ":
          tic_map[pos] = "O"

         return tic_map

aser=put_abatar

def put_AI(tic_map):
    import random
    while True:
     pos= random.randrange(9)
     if tic_map[pos] == " ":
         tic_map[pos] = "X"
         return tic_map

aser = make_map()


for i in range(100):
    print_map(aser)
    aser=put_abatar(aser)
    aser=put_AI(aser)

