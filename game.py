import random

comp_wins = 0
player_wins = 0

def Choose_Option():
	user_choice = input("Choose Rock,Paper or Scissors!!!")
	if user_choice in ["Rock","rock","R","r"]:
		user_choice = "r"
	elif user_choice in ["Paper","paper","P","p"]:
		user_choice = "p"
	elif user_choice in ["Scissors","scissors","S","s"]:
		user_choice = "s"
	else:
		print("I dont understand , try to choose among given options only")
		Choose_Option()
	return user_choice

def Computer_Option():
	comp_choice = random.randint(1,3)
	if comp_choice == 1:
		comp_choice = "r"
	elif comp_choice == 2:
		comp_choice = "p"
	else:
		comp_choice = "s"
	return comp_choice

while True:
 print("")
 user_choice = Choose_Option()
 comp_choice = Computer_Option()
 print("")

 if user_choice == "r":
  if comp_choice == "r":
   print("you chose rock.the computer chose rock.so its a tie!!!")
  elif comp_choice == "p":
   print("you chose rock and computer chose paper.computer won!!!")
   comp_wins += 1
  elif comp_choice == "s":
   print("you chose rock and computer chose scissors.you won!!")
   player_wins += 1

 elif user_choice == "p":
  if comp_choice == "r":
   print("you chose paper and computer chose rock.you won!!")
   player_wins +=1
  elif comp_choice == "p":
   print("you chose paper and computer chose paper. so it is a tie!!!")

  elif comp_choice == "s":
   print("you chose paper and computer chose scissors. so computer won!!")
   comp_wins += 1

 elif user_choice == "s":
  if comp_choice == "r":
  	print("you chose scissors and computer chose rock. so computer won!!")
  	comp_wins += 1
  elif comp_choice == "p":
  	print("you chose scissors and computer chose paper. so you won!!")
  	player_wins += 1
  elif comp_choice == "s":
  	print("you chose scissors and computer chose scissors.so it is atie!!")

 print("")
 print("Player wins:" + str(player_wins))
 print("Computer wins:" + str(comp_wins))
 print("")

 user_choice = input("do you want to play again?(y/n)")
 if user_choice in ["Y","y","yes","Yes"]:
 	pass
 elif user_choice in ["N","n","No","no"]:
 	break
 else:
 	break
