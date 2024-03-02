print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Quest.\n")
print("You must find the treasure, or die trying!")
print("Will you enter the dungeon, or live to see another day?")
choice1 = input('Type "Enter" or "Leave" now. \n').lower()

if choice1 == "enter":
    print("Has the dungeon found it's next victim?")
    
    print("You see two halls, which do you choose?")
    choice2 = input('Type "Left" or "Right". \n').lower()
    if choice2 == "left":
        print("You find a suit of armor with a button on the chest plate.")
        choice3 = input('Do you "press" the button, or "walk" past?\n').lower()
        if choice3 == "press":
            print("A trap door opens and you land in the treasure. How can you escape?")
        else:
            print("The suit comes to life as you turn your back....it's too late.")
            print("Game Over!")
    else:
        print("You walk into a room full of zombies.")
        print("Game Over!")
else:
    print("You have decided to live another day, for now.")