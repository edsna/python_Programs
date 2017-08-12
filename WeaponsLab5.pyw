#Weapons Program
#Edson & Francisco

#This program is designed to prompt a user to enter the kind and amount of weapons they have and display the amount left after throwing


#Variables
#Weapons_List
WeaponType = 0
AmountWeapon = 0
LowestValue = 0
Weapons_List = []
AmountWeapons = [] 
ExitLoop = "done"
Done = "done"

#Weapon type is not limited to inputs with only a-z characters because there's weapons that have numbers in their names (i.e. AK 47)
#Following Code creates the  list of Weapons users will be introducing
WeaponType = raw_input("Enter weapon type: ")
while WeaponType != ExitLoop:
  
        AmountWeapon = input("Amount of weapon: ")
        if AmountWeapon <0:
          print "Error!! Enter a Non-negative Amount of Weapon!"
        else:
            Weapons_List.append(WeaponType)
            AmountWeapons.append(AmountWeapon)
            WeaponType = raw_input("Enter weapon type: ")
#First While Loop aranjes and displays the list of weapons users introduced and prompts them to subtract their weapons and does so or not accordingly followed by a last not being thankfull for the user to have used the system
while len (Weapons_List) > 0:
  ThrowPrompt = raw_input("Would you like to throw your Weapons? ")
  if ThrowPrompt == "Yes":
    for abcd in range(0,len(Weapons_List)):
        print abcd + 1,".", Weapons_List[abcd]
        
    Throw = input ("Which weapon would you like to throw? Insert the integer of the weapon you'd like to use: ")
    while Throw != Done:
      print "You chose", Weapons_List[Throw-1]
      Weapon = Weapons_List[Throw-1] 
      NumberThrow = input("How much would you like to throw?: ")
      if (AmountWeapons[Throw-1] > NumberThrow) and (NumberThrow > 0):
          AmountWeapons[Throw-1] = AmountWeapons[Throw-1] - NumberThrow
      elif (AmountWeapons[Throw-1] == NumberThrow) and (NumberThrow > 0):
          AmountWeapons.pop(Throw-1)
          Weapons_List.pop(Throw-1)
          print "You exhausted the total number of", Weapon , "available."
      elif AmountWeapons[Throw-1] < NumberThrow:
          AmountWeapons.pop(Throw-1)
          Weapons_List.pop(Throw-1)
          print "You exhausted the total number of the weapon. Although you entered a value over the actual value, the weapon was exhausted."
      elif (LowestValue >= NumberThrow):
          print "Invalid input"
      elif len (Weapons_List) == 0:
        print "Game over. Thank you for playing"
      #print "Thank you for playing!"
      print "You have: ", AmountWeapons[Throw-1], Weapons_List[Throw-1], "Left"
      ContinueThrowing = raw_input("Would you like to throw more guns? ")
      if ContinueThrowing == "Yes":
        Throw = input ("Which weapon would you like to throw? Insert the integer of the weapon you'd like to use: ")
      else:
        break
  else:
    break
print "Thank you for playing!"
print "GAME OVER"
