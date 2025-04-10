print("Welcome to treasure island")
print("Your mission is to find the lost treasure")
choice1 = input('You\'re at a cross road.' \
' Where do you want to go? Type "left" or "right" ').lower()
if choice1 == "left":
     choice2 = input('You have come to a lake.' \
     'There is an island in the middle of the lake.' \
     'Type "wait" to wait for a boat.' \
     'Type "swim" to swim across. ').lower()
     if choice2 == "wait":
          choice3 = input('You arrive at the island unharmed.'\
                         'There is a house with 3 doors.One red, one yellow and one blue.'\
                         'Which colour do you choose?').lower()
          if choice3 == "red":
               print("Its a room full of fire, Game over")
          elif choice3 == "yellow":
               print("You found the treasure! You Win!")
          elif choice3 == "blue":
               print("You entere a room full opf beasts. Game over")
     else:
          print("you choose a room that does not exist, Game over")
else: 
     print("You fall into a hole.Game Over.")   
