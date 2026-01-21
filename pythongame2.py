import random
actiune = 0
happiness = 50
money = 0
energy = 100
bani = 0
loculactiunii = 0
loculactiuniiziua = 0



def diminiata():
    global actiune
    for actiune in range(1, 2):
        global energy
        print("buna diminiata")
        actiune = int(input("ce vrei sa faci- 1 - faci patul sau 2-stai pe tiktok"))
        if actiune == 1:
            energy = random.randint(5,20)
        elif actiune == 2:
            energy = random.randint(-15,-5)
        else:
            diminiata()
        print("energia ta este acum:" , energy , "Cash" , money , "fericire", happiness )
        print("**************************************************************")

def actiunedupatrezire():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("teai sculat din pat")
        actiune = int(input("Ce alegi- 1-sa faci rutina zilnica sau 2-te duci sa mananci(o sa puta de la tine)"))
        if actiune == 1:
            energy = random.randint(0,40)
        elif actiune == 2:
            energy = random.randint(-20,0)
        else:
            actiunedupatrezire()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")

def actiunedupaobed():
    global energy,money,happiness,actiune,loculactiunii
    for loculactiunii in range(1, 2):
        print("vrei sa pleci cu prietenii la o bere")
        actiune = int(input("Ce alegi 1- pleci cu kentii la o bere sau 2-mergi la scoala"))
        if loculactiunii  == 1:
            energy = random.randint(-5,25)
            happiness = random.randint(0,40)
        elif loculactiunii == 2:
            energy = random.randint(-15,0)
            happiness = random.randint(-30,5)
        else:
            actiunedupaobed()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")

def cupatanii():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print('ai plecat cu patanii dupa piva dar nai bani')
        actiune = int(input("Ce faci 1-ceri de la parinti(vor afla ca te duci dupa bere i vei manca usigani) sau 2- ceri de la bratani"))
    if actiune == 1:
        energy -= energy
        happiness -= happiness
        print("parintii ti-au dat usigane si nu tiua dat voie sa iesi din casa timp de saptamana")
    elif actiune == 2:
        energy = random.randint(13,37)
        happiness = random.randint(-5,25)
    else:
        cupatanii()
    print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
    print("**************************************************************")


def dupapiva():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("vrei sa mananci")
        actiune = int(input("Ce alegi 1-pleci fara bani cu patanii la kebab si ei iara in dolg sau 2-te duci sa furi din banca"))
        if actiune == 1:
            energy = random.randint(10,20)
            happiness += 30
            money = random.randint(0,10)
            print("patanii dama so zaibit sa-ti di-a in dolg,dar ca real friend o sa te ajute")
        elif actiune == 2:
            energy = 20
            happiness += random.randint(10,100)
            money = random.randint(100000,10000000)
            print("patanii o zis ca esti sigma + 10000 aura")
        else:
            dupapiva()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")

diminiata()
actiunedupatrezire()
actiunedupaobed()
cupatanii()
dupapiva()

##################################### GO TO SCHOOL #################################################


def lectia3():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("totusi ati facut cu patanii veselie si acum nu aveti ce face si va duceti la scoala,diriginta a intrebat unde ati fost")
        actiune = int(input("Ce spuenti 1-ati ajuatat toti ipreuna sa treaca bunica peste drum sau 2-Ati dat vaccina pe armata"))
        if actiune == 1:
            energy += 10
            happiness += 20
        elif actiune == 2:
            energy += 20
            happiness += 30
        else:
            lectia3()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")


def pauzadupalectia3():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("ti sa facut rau de la kebab")
        actiune  = int(input("Ce faci 1- de duci repede pana acasa(sansa ca o sa ajungi este 50/50%) 2- de duci la doctor"))
        if actiune == 1:
            print("ti-ai adus aminte ca ai rubla si te-ai chemat un vertolet pana acasa")
            energy += 40
            happiness += 50
            money -= random.randint(-1000,-10000)
        elif actiune == 2:
            print("doctorul nu era si te-ai cacat pe tine")
            energy -= 20
            happiness -= random.randint(-50,-120)
        else:
            pauzadupalectia3()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")


def dupaviceu():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("tu nu vrei la scoala,dar nu stii ce sa faci")
        actiune = int(input("Ce faci 1-intrii pe 1win si joci un pic sau 2-te joci  in pc"))
        if actiune == 1:
            print("Din start ai ineput sa castigi dar pentru ca cazicul este doar o minciuna ai inceput sa pierzi ")
            energy = random.randint(0,50)
            happiness -= 30
            money -= random.randint(-10000,100000)
        elif actiune == 2:
            energy += 10
            happiness += 40
        else:
            dupaviceu()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")


def ora3():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("din cauza ca ai furat din bank pe tine te cautau,tu ai lasat prea multe indicii si pe tine teau gasit politia")
        actiune = int(input("Ce alegi 1-te predai sau 2-il chemi pe hulk cu ajutorul a 500 de mii de lei ca sa te ajute"))
        if actiune == 1:
            energy -= random.randint(-20,-40)
            happiness -= 50
        elif actiune == 2:
            energy += 10
            happiness += 40
            money -= random.randint(-250000,-500000)
        else:
            ora3()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")


def dupafight():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("hulk i-a chistigat pe toti dar totusi tu mai ramai cautat de politie iar hulk nu mai poate sa de ajute pentru ca sa dus sa di-a gambling")
        actiune = int(input("ce faci 1-iti ei vertaliotul si kentii si pleci intro alta tara lasand parintilor  o parte din suma sau 2-ramai aici"))
        if actiune == 1:
            energy = random.randint(-20,-100)
            happiness -= random.randint(-25,-100)
            money = random.randint(-200000,-300000)
        elif actiune == 2:
            print("pe tine te-au gasit din nou acum nare cine sa te ajute,ai ajuns in inchisoare")
            energy -= energy + 10
            happiness -= happiness + 10
            money -= money
        else:
            dupafight()
        print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
        print("**************************************************************")

lectia3()
pauzadupalectia3()
dupaviceu()
ora3()
dupafight()


################################################################ Happy end  ############################################################################

def ladubei():
    global energy,money,happiness,actiune
    for actiune in range(1, 2):
        print("acum esti liber ai luat cu patanii o casa in chirie,acum patanii eu de la tine in dolg dar tu ca un real bro ii ajuti si acum traiesti fericit")
        actiune = int(input("e deja taziu ce faceti 1-faceti nani sau 2-faceti nani"))
    if actiune == 1:
        energy += random.randint(15,100)
        happiness += random.randint(10,70)
    elif actiune == 2:
        energy += 100
        happiness += random.randint(5,50)
    else:
        ladubei()
    print("energia ta este acum:", energy, "Cash", money, "fericire", happiness)
    print("**************************************************************")

ladubei()



