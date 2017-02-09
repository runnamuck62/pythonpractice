#Pokemon Game

#TODO: 
#		Make 3 moves that do damage/healing
#		Set players health and a function that subracts it
#		Let the player choose a move
#		Let the AI choose a move
#		Subract the moves from health


from random import randint



player_health = 100
ai_health = 100




#This is the players turn put into one function
def player_move():
	global player_health
	global ai_health
	attack_choices = ["light" , "heavy" , "heal"]
	#player chooses which attack to do
	move = input("What do you want to do? (Light, heavy, heal): ")
	while move not in attack_choices:
		move = input("That is not a valid choice. Choose again:  ")		#light heavy and heal are given a random int assigned and it is added or subtracted from correct player
	print()
	if move == "light":
		damage = randint(15,30)
		ai_health -= damage
		print("You did" ,damage, "damage.")
	elif move == "heavy":
		damage = randint(19,24)
		ai_health -= damage
		print("You did", damage, "damage.")
	elif move == "heal":
		heal = randint(10,20)
		player_health += heal
		print("You healed for" ,heal , "hit points") 
	if ai_health >= 0:
		print("The AI has" ,ai_health ,"Health, and you have" ,player_health ,"health.")
		print()
	else:
		print("The AI has 0 Health, and you have" ,player_health ,"health.")
		print()
		

#This function is the AI's move
def ai_move_normal():
	global player_health
	global ai_health
	attack_choices = ["light" , "heavy" , "heal"] 		#Puts the AI choices in a library for it to choose from
	move = attack_choices[randint(0, 2)] 				#Chooses a random index in the library
	if move == "light":
		damage = randint(15,30)
		player_health -= damage                  		 
		print("The AI chose" , move )
		print("The AI did" ,damage , "points of damage")
	elif move == "heavy":
		damage = randint(19,24)
		player_health -= damage
		print("The AI chose" , move )
		print("The AI did" ,damage , "points of damage")
	elif move == "heal":
		heal = randint(10,20)
		ai_health += heal
		print("The AI chose" , move )
		print("The AI healed for" ,heal, "hit points")  
	if player_health >= 0:
		print("The AI has" ,ai_health ,"Health, and you have" ,player_health ,"health.")
	else:
		print("The AI has" ,ai_health ,"Health, and you have 0 health.")
	print()
	print("-----------------------------------------") 


#This function is run if the AI is below 30 health. It prioritizes heal.
def ai_low_health():
	global player_health
	global ai_health
	attack_choices = ["light" , "heavy" , "heal", "heal"] 			#Heal has an addition index in this library
	move = attack_choices[randint(0, 3)] 							#The random range is extended. Everything else is the same
	if move == "light":
		damage = randint(15,30)
		player_health -= damage
		print("The AI chose" , move )
		print("The AI did" ,damage , "points of damage")
	elif move == "heavy":
		damage = randint(19,24)
		player_health -= damage
		print("The AI chose" , move )
		print("The AI did" ,damage , "points of damage")
	elif move == "heal":
		heal = randint(10,20)
		ai_health += heal
		print("The AI chose" , move )
		print("The AI healed for" ,heal, "hit points")  
	if player_health >= 0:
		print("The AI has" ,ai_health ,"Health, and you have" ,player_health ,"health.")
	else:
		print("The AI has" ,ai_health ,"Health, and you have 0 health.")
	print() 
	print("-------------------------------------")

#Not sure if this works, but these two turns determine how the AI acts. If it is below 30 health, it should choose to heal more often
def turn_normal():
	while player_health > 0 and ai_health > 30:
		player_move()
		if ai_health <= 0:
			print("You WIN!!")
			break
		ai_move_normal()
		if player_health <= 0:
			print("AI Wins!!")
			break
		if ai_health < 30:
			turn_low_health()
			
def turn_low_health():
	while player_health > 0 and ai_health <= 30:
		player_move()
		if ai_health <= 0:
			print("You WIN!!")
			break
		ai_low_health()
		if player_health <= 0:
			print("AI Wins!!")
			break
	if ai_health >= 30:
		turn_normal()
		
def main():
	turn_normal()
	
main() 
	

			






