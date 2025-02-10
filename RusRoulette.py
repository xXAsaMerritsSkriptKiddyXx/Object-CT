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
revolver = Weapon("1887 New Model Army", 6, 1, 80)
shotgun = Weapon("Remington 700", 8, 3, 120)
bobsemple = Weapon("M1A2 Abrams", 29, 20, 3500)
gau21int = Weapon("M61A1 Vulcan", 964, 700, 560)

weaponlist = ["rubberband" = rubberband, "revolver" = revolver, "shotgun" = shotgun, "bobsemple" = bobsemple, "gau21int" = gau21int]
#List used in selection of weapon at start of game.

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
             wchoc = input("What weapon would you like to use?:") 
             if wchoc in weaponlist():
                print("You have selected: \n", weapon.name)
        elif res in han:
            print("\n Then..")
            time.sleep(1)
            print("GET OUT! \n")
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
             + "\nand " + player.name + " takes " + weapon.damage + " damage!")
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

main() 
