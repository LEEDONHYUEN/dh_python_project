import random
class makeCH():

    def __init__(self):
        self.hp = random.randrange(100, 150)
        self.mp = random.randrange(170, 200)
    def hit (self):
        return self.hp *0.5
    def heal(self):
        self.hp=self.hp+20.0
        self.mp=self.mp-20.0
    def fire_ball(self):
        return self.hp *0.8
    def nuclear_power(self):
        return self.hp *1.0



a=makeCH()
print("a character hp : {} , mp : {}".format(a.hp, a.mp))

b=makeCH()
print("b character hp : {} , mp : {}".format(b.hp, b.mp))

while True:
    usert= input("hit 또는 heal 또는 fire_ball 또는 nuclear_power을 입력하세요")
    if usert == "hit":
        b.hp=b.hp-a.hit()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    if usert == "heal":
        a.heal()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    if usert == "fire_ball":
        b.hp=b.hp-a.fire_ball()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    if usert == "nuclear_power":
        b.hp = b.hp - a.nuclear_power()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    airt=random.randrange(1,5)
    if airt ==1:
        a.hp=a.hp-b.hit()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    if airt ==2:
        b.heal()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    if airt ==3:
        a.hp = a.hp - b.fire_ball()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    if airt ==4:
        a.hp = a.hp - b.nuclear_power()
        print("a character hp : {} , mp : {}".format(a.hp, a.mp))
        print("b character hp : {} , mp : {}".format(b.hp, b.mp))
    if a.hp<=0 or b.hp<=0:
        print("the game was stoped by administer")
        break
    if a.mp<=0 or b.mp<=0:
        print("you are not able to use mp")
        break
print("Who did become winner?")
print("Which player did you bet your money?")
print("If your player became winner, you can be a rich man")
print("If your player became loser, you will be killed by some mean guy just like 오징어게임")
print("If you will be dye, we are going to burn you")
print("Hahahaha")


