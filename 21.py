# A variation of the game 21
#Idea from reddit.com/r/beginnerprojects
# https://www.reddit.com/r/beginnerprojects/comments/19ot36/project_a_variation_of_21/
#Created by Ben Nichols on 2/9/17

from random import randint
starting_score = 100													#The point total for the round

#The function that does all the work. It dictates what happens each round
def  draw_cards():
	global starting_score
	cards = list(range(1 , 14)) * 4              						#Building a deck of cards. Makes a lis of numbers between 1-13 , 4 times for a total of 52 cards												#The starting score that you have. Changes at the end of every rounds
	total = 0 															
	while total < 21:													#While you don't go over 21, it keeps asking if you want to hit
		hit = input("Hit or stop?: ").lower() 
		if hit == "hit":
			random_card = cards[randint(1 , len(cards) - 1)]			#Draws a random card from "cards"
			if random_card == 1:										#This assigns face card values. Want to find a better way
				print("Ace")
			elif random_card == 11:
				print("Jack")
			elif random_card == 12:
				print("Queen")
			elif random_card == 13: 
				print("King")
			else: 
				print(random_card)
			del cards[random_card]										#Deletes the card chosen from the deck
			total += random_card 										#Adds the value of the card drawn to the total points for the round
			print("Total: " , total)
			print() 
		else: 
			starting_score = starting_score - (21 - total)				#Anything other than hit ends the round and the difference between 21 and your total is
			break 														#subtracted from your starting score
	if total == 21:
		print("21 reached. Starting new round")							#If you hit 21, nothing gets taken from your score
	elif total > 21:													#If you bust, you subtract 21 from your score.
		print("Bust. Starting new round") 
		starting_score -=21 
	print("points remaining: " , starting_score )
	print()
	
	
	
def main():
	for i in range(1, 6):												#Runs the function for 5 rounds
		print("Round" , i )	
		print()
		draw_cards()  
		
	print("Final Score: " , starting_score) 

main() 


 
