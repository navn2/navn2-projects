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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Monk's Treasure Island.")
print("Your mission is to find the legendary Monk's treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
user_data=input("you are at a crossroad. where do you want to go? Type 'left' or 'right'")
choice=user_data.lower()
if choice=="left":
          print("You have come to a lake. There is an island in the middle of the lake.")

          user_data=input("Type 'wait' to wait for a boat. Type 'swim'to swim across.")
          choice=user_data.lower()
          if choice=="wait":
                    print("You have reached the island. You have three doors in front of you. One red, one yellow and one blue.")
                    user_data=input("Which door you wish to open? Type 'red', 'yellow' or 'blue'.")
                    choice=user_data.lower()
                    if choice=="yellow":
                              print("You have reached the treasure, It is all yours. YOU WIN.")
                    elif choice=="red":
                              print("You have been burnt by lava. the GAME IS OVER.")
                    elif choice=="blue":
           
                              print("You have been eaten by a deadly beast. the GAME IS OVER.")
                    else:
                              print("You have acted suspicous on the island. You lose. the GAME IS OVER.")
          else:  
                    print("You have drowned in a whirlpool. The GAME IS OVER.")
else:
          print("You ended up in a forest. You are lost. The GAME IS OVER.")
          