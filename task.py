print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
cross_road = str(input("\tType \"left\" or \"right\"\n"))

if cross_road.lower() == "right":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = str(input("\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n"))
    if lake.lower() == "wait":
        print("You've arrived at the island unharmed. There is a house with 3 doors.")
        door = str(input("\tOne red, one yellow and one blue. Which color do you choose?\n"))
        if door.lower() == "red":
            print("You are burning in the fire!!!....Game Over!")
        elif door.lower() == "blue":
            print("You've been attacked by the beasts....Game Over!")
        elif door.lower() == "yellow":
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("You've been attacked by the trout....Game Over!")
else:
    print("You've fallen into a hole....Game Over!")