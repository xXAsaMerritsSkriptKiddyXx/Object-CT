import random, sys, time

def Funnyquit():
 print("\n Then..")
 time.sleep(1)
 print("GET OUT! \n")
 time.sleep(1)
 sys.exit()      

# Blueprint for different weapons.
class Weapon:
    def __init__(self,
        type = "1886 New Model Army", 
        name = "revolver",
        shells = 6,
        liveR = 1,
        damage = 80
    ):
        self.type = type
        self.name = name
        self.shells = shells
        self.liveR = liveR
        self.damage = damage

rubberband = Weapon("Rubber Band Launcher", "rubberband", 30, 2, 2 )
revolver = Weapon("1887 New Model Army","revolver", 6, 1, 100)
shotgun = Weapon("Remington 700","shotgun", 8, 3, 120)
bobsemple = Weapon("M1A2 Abrams","bobsemple", 29, 20, 3500)
gau21int = Weapon("M61A1 Vulcan","gau21int", 964, 700, 560)

options = {
    "rubberband" : rubberband,
    "revolver" : revolver,
    "shotgun" : shotgun,
    "bobsemple": bobsemple,
    "gau21int" : gau21int
}
# Dictionary for Weapon Options

weapons = []
weapons.append(rubberband)
weapons.append(revolver)
weapons.append(shotgun)
weapons.append(bobsemple)
weapons.append(gau21int)
# List for Weapon Options.
# Combo of List and Dictionary gives optoins on which to refer to. 

selwep = []
hitc = 0

class Player:
    def __init__(self,
        name = "You",
        health = 100,
        x = True
):
        self.name = name
        self.health = health
        self.x = x

user = Player()

class Bot:
    def __init__(self,
        bname = "Evan Michael Merritt",
        bhealth = 100,
        y = False,
        qchance = 3
):
        self.bname = bname
        self.bhealth = bhealth
        self.y = y
        self.qchance = qchance
# x and y are used to iterate between whose turn it is.
comp = Bot()

sey = ["yes", "y"]
han = ["n", "n"]

def main():
    global selwep
    s = 1
    if s == 1:
        print("Hello. Welcome to Russian Roulette. Where your bravery will be put to the test.")
        time.sleep(1)
        print("Would you like to continue?")
        res = input("Y/N: \n").strip().lower()
        if res in sey:
             run = True
             while(run):
                print("Please pick a weapon: \n")
                # for w, weapon in options.items():
                #     print(w)
                # userin = input().strip().lower()
                for i, weapon in enumerate(weapons):
                    print(i+1, weapon.name)

                userin = input().strip().lower()
              

                if userin.isnumeric() and int(userin) <= len(weapons):
                     selwep = weapons[int(userin)-1]
                     print("\n You have chosen:" , selwep.type, "\n") 
                     if input("Would you like to go first? \n") in sey:
                        user.x = True
                        comp.y = False
                        trigger()
                     else:
                        comp.y = True
                        user.x = False
                        trigger()
                     run = False
                else:
                 print("Please return an integer from the allowed list!")
                # if userin in options.keys():
                #     print(options[userin].type)
                #     break
        elif res in han:
            Funnyquit()
        else:
             print("Please return a valid answer between Yes or No.")
             #main()


def trigger():
    global hitc
    sh = 0
    while sh <= selwep.shells:
        if user.x == True and comp.y == False:
            firc = input("Fire? \n Y/N:")
            if firc in sey:
                hitc = random.randint(0, selwep.shells)
                if hitc <= selwep.liveR:
                    print("The " , selwep.type, "goes off") 
                    time.sleep(1) 
                    print(user.name + " take " + str(selwep.damage) + " damage!")
                    user.health = (user.health - selwep.damage)
                    sh += 1
                    user.x = False
                    comp.y = True 
                    #Only runs at end of game
                    if user.health <= 0:
                        print(user.name + " have gone kablooey.\n ")
                        if input("Would you like to play again?\n Y/N") in sey:
                            quit
                            main()
                        elif input() in han:
                         Funnyquit()
                        else:
                            print("Please reutrn a valid answer. \n")
                
                if hitc > selwep.liveR:
                    print("Nothing happened")
                    sh += 1
            #Only runs if you decide not to fire
            if firc in han:
             Funnyquit()
            else:
             print("Please return a valid response: \n")   
        else:
            #Bot coding
            if comp.y == True and user.x == False:
                 quitp = random.randint(0,20)
                 if quitp <= comp.qchance:
                     print("Your opponent forefits! \n")
                     input("Would you like to play again?")
                     if input() in sey:
                         quit
                         main()
                     if input() in han:
                         Funnyquit()
                 else:
                     if hitc <= selwep.liveR:
                         print("The " , selwep.type, "goes off") 
                         time.sleep(1) 
                         print(comp.bname + " takes " + str(selwep.damage) + " damage!")
                         comp.bhealth = (comp.bhealth - selwep.damage)
                         sh += 1
                         user.x = True
                         comp.y = False
                         #Only runs at end of game
                         if comp.bhealth <= 0:
                             print(comp.bname + " has gone kablooey.\n ")
                             if input("Would you like to play again?\n Y/N") in sey:
                                 quit
                                 main()
                             elif input() in han:
                                 Funnyquit()                         
                             else:
                                 print("Please reutrn a valid answer. \n")
    #Runs if all shells go off and no one wins
    if sh > selwep.shells:
        if input("Would you like to play again?\n Y/N") in sey:
         quit
         main()
        elif input() in han:
         Funnyquit()
        else:
         print("Please reutrn a valid answer. \n")



if __name__ == "__main__":
    main() 
