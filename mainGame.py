print("You wake up in a cold room feeling tired.")
print("It is dark, you can not see anything.")
print("As you are trying to re-collect your memories lights turn on")
print("You finally remember where you are.")
print("You are in space")
print("Your body has been frozen for the past 69 years.")
print("Are you ready to play?")
playChoice = input("> ")

if(playChoice == "yes"):
  print("The lights flicker and an alarm sounds.")
  print("A voice on the intercom turns on")
  print("Please make your way to the center of the ship")
  print("Violation of this instruction will lead to punishment")
  print("Do you listen?")
  ListenChoice1 = input("> ")

  if(ListenChoice1 == "yes"):
    print("You make your way to the center using signs.")
    print("You are briefed on the planet you are going to.")
    print(".It is called Plantet X")
    print(".It has no known forms of intelligent life.")
    print(".However, there are many deadly beasts.")
    print(".They range from the size of a dog to the size of a whale. ")
    print("You will be landing shortly.")
    print("Will you take a seat?")
    landChoice1 = input("> ")
    if (landChoice1 == "yes"):
      print("You have landed.")
      print("You are injected with a fluid in your neck")
      print("The syringe has a number that says 69420")
      print("The rest of your memories start rushing back to you.")
      print("As you look around seemingly suprised, you notice a number tatooed on your arm.")
      print("69420")
      print("It all makes sense now. That is my number.")
      print("You see a man dressed in a combatant uniform.")
      print("His badge reads Major General")
      print("He introduces himself and tells you he is brigade Commander of the 69th Mechanized Brigade.")
      print("He throws a combat uniform on your bed and tells you to get ready.")
      print("You are briefed.")
      print(".When they said there was no intellegent life")
      print(".That was a lie.")
      print(".We knew many of you would be reluctant to cooperate if you knew there was intelligent life.")
      print(".You are free to leave if you do not want to continue.")
      print("Do you leave the room?")
      leaveRoom1 = input("> ")
      if (leaveRoom1 == "yes"):
        print("You are shot to death after leaving the room.")
        exit()
      elif (leaveRoom1 == "no"): 
        
        print("About a 4th of the people walk out.")
        print("You hear gunshots and screams outside the room.")
        print(".Anyone else? The commander asks.")
        print("The room is silent..")
        print(".Good")
        print("Do you want to continue playing the game?")
        continuePlaying1 = ("> ")
        if (continuePlaying1 == "yes"):
          print(".We will be attacking the aliens.")
          print(".We will be divided into 4 main mechanized untis. ")
          print("")

        elif (continuePlaying1 == "no"): 
          print("Thats fine!")
          exit()
          #bug here
        
        else: 
          print("Invalid answer. Please type yes or no.") 
          exit()
          #bug here

          #when you type "no" it prints "Invalid answer. Please type yes or no." instead of "Thats fine!" It still exits so it is functional but it is inconvinient. 
          
          
          
        
      

    
    elif (landChoice1 == "no"):
      print("You have died on impact.")
      exit()

    else:


      
      print("Invalid answer. Please type yes or no.")
    
  elif(ListenChoice1 == "no"):
    print("You go to explore the ship and you are marked absent.")
    print("You are caught by an unarmed guard who sounds an alarm. run or fight.")
    caughtChoice1 = input("> ")
    if (caughtChoice1 == "fight"):
      print("You are overpowered! You are put in jail for 5 days")
      print("A fellow prisoner has offered you some money to steal a key and help him escape.")
      print("This can get you in a lot of trouble.")
      print("Will you do it?")
      steal1 = input("> ")
      if (steal1 == "yes"): 
        print("You have been caught! You have been put in high security prison until you land which you will then be forced into labor for your crimes.")
        print("You hear over the intercom that the ship will be landing soon. You are transported to a seating area.")
        print("The ship lands...")
        print("You are forced into construction for your crimes.")
        print("You notice the supervisor sleeping. Do you run?")
        escape2 = input("> ")
        if (escape2 == "yes"):
          print("You have escaped into the alien forest.")
          print("You run into a creature that seems agressive. It is about the size of a dog.")
          print("Do you fight or run?")
          fightChoice2 = input("> ")
          if (fightChoice2 == "fight"):
            print("You killed the beast")
            print("You collect it's meat to eat for later.")
            print("It is now night time. Make a fire?")
            fireChoice1 = input("> ")
            if (fireChoice1 == "yes"):
              print("You made a fire.")
              print("The smoke draws attention to law enforcement")
              print("You are woken with a gun to your head with police yelling at you.")
              print("You are under arrest")
              print("Do you escape?")
              escapeChoice3 = input("> ")
              if (escapeChoice3 == "yes"):
                print("You get killed")
                exit()
              elif (escapeChoice3 == "no"):
                print("You are arrested and sent to prison")
              else: 
                print("Invalid answer. Please type yes or no.")
                

            elif (fireChoice1 == "yes"):
              print("You decide not to make a fire")
              print("The temp drops to -69F")
              print("You freeze to death")
            else: 
              print("Invalid answer. Please type yes or no.")

          elif (fightChoice2 == "run"):
              print("You get chased and killed by the beast.")
              exit()
        

        
            

        elif (escape2 == "no"):
          print("You choose not to escape.")

        else: 
          print("Invalid answer. Please type yes or no.")
          
                
            
      elif (steal1 == "no"):
          print("You have declined the offer.")

      else:
        print("Invalid answer. Please type yes or no.")
          
      
        
        
    elif(caughtChoice1 == "run"):
        print("You have escaped the guard!")
        print("You find a box that has switches. do you touch them?")
    touchChoice1 = input("> ")
    if (touchChoice1 == "yes"):
      print("You have turned off the oxygen.")
      exit()
    elif (touchChoice1 == "no"):
        print("You don't touch the switches.")
        print("Over the intercom you hear that the ship will land soon.")
        print("You will likely die if you do not find the seating area.")
        print("Do you look for the seating area?")
        lookChoice1 = input("> ")
        if (lookChoice1 == "yes"):
          print("You barely make it to the seating area.")
          print("You land")
          print("You get thrown in a prison for life on the planet for violations.")
          print("Do you try to escape?")
          escapeChoice1 = input("> ")
          if (escapeChoice1 == "yes"):
            print("You get caught and you are executed for your crimes.")
            exit()
          elif (escapeChoice1 == "no"):
            "You are thrown in prison for life! You lost!"
            exit()
          else:
            print("Invalid answer. Please type yes or no.")

          if (lookChoice1 == "no"):
            print("You have died on impact!")
            exit()
          
      
    else:
    
      print("Invalid answer. Please type yes or no")
    
  else:
    print("Invalid answer. Please type yes or no")
  
elif(playChoice == "no"):
  print("The game has ended because you said no.")
  exit()
else:
  print("Invalid answer. Please type yes or no")
  

  

