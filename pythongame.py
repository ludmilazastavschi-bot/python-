import random


health_player = 100
atack_player = 15


health_enemy = random.randint(100,200)
atack_enemy  = random.randint(10,20)


turn = 1


def atack():
        global health_enemy, turn
        if turn ==1:
         health_enemy -=atack_player + random.randint(1,5)
        turn = 2
        if health_enemy <=0:
            print("ai castigat")
            exit()

        choice()

def health_playerr():
        global health_player, turn
        if turn == 1:
            health_player += random.randint(10,20)
        turn = 2
        if health_player > 100:
             health_player = 100

def atack_enemyy():
    global health_player, turn
    health_player -= atack_enemy
    if health_player <=0:
        print("ai pierdut")
        exit()
    turn = 1


def heal_enemy():
    global health_enemy, turn
    health_enemy += random.randint(1,10)
    turn = 1
def choice():
    c = random.randint(1,2)
    if c ==1:
         atack_enemyy()
    elif c == 2:
        heal_enemy()


def optiuniii():
    print("Viata jucator: ", health_player, "viata inamic:  ", health_enemy)
    print("1 - Atack")
    print("2 - Heal")
    print("3 - Leave game")

while True:
    optiuniii()
    n = int(input("ce optiuni alegi:"))
    if n == 1:
        atack()
    elif n == 2:
         health_playerr()
    elif n == 3:
        print("la revedere")
        break
    else:
        print("ati scris gresit")
