import random 
import time

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
revolver = Weapon("1887 New Model Army","revolver", 6, 1, 80)
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

class Player:
    def __init__(self,
        name = "You",
        health = 200,
        x = 0
):
        self.name = name
        self.health = health
        self.x = x

class Bot:
    def __init__(self,
        bname = "Evan Michael Merritt",
        bhealth = 200,
        y = 1,
        qchance = [3,10]
):
        self.bname = bname
        self.bhealth = bhealth
        self.y = y
        self.qchance = qchance
# x and y are used to iterate between whose turn it is.


sey = ["YES", "Y"]
han = ["NO", "N"]

def main():
    s = 1
    if s == 1:
        print("Hello. Welcome to Russian Roulette. Where your bravery will be put to the test.")
        time.sleep(1)
        print("Would you like to continue?")
        res = input("Y/N: \n").strip().upper()
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
                     print("\n You have chosen:" , weapons[int(userin)-1].type, "\n") 
                     run = False
                else:
                 print("Please return an integer from the allowed list!")

                # if userin in options.keys():
                #     print(options[userin].type)
                #     break
        elif res in han:
            print("\n Then..")
            time.sleep(1)
            print("GET OUT! \n")
            time.sleep(1)
            s = 1
            quit           
        else:
             print("Please return a valid answer between Yes or No.")


def trigger():
    sh = 0
    if sh < weapon.shells:
        hitc = random.randint(1, weapon.shells)
        if hitc <= weapon.liveR:
             print("The " , weapon.type, "goes off", time.sleep(1) 
             + "\nAnd " + player.name + " takes " + weapon.damage + " damage!")
             player.health = (player.health - weapon.damage)
             sh += 1
             if player.health <= 0:
                 print(player.name + " Has gone kablooey.\n ")
                 if input("Would you like to play again?\n Y/N") == "Y":
                     main()
                 elif input() == "N":
                     quit
                 else:
                     print("Please reutrn a valid answer. \n")
        if hitc > weapon.liveR:
            print("Nothing happened")
            sh += 1


if __name__ == "__main__":
    main() 
