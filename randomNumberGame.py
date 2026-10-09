playerAnswer=10000
tries=0
import random
range=input("How Hard?: ")
range=int(range)
answer=random.randint(0,range)
while playerAnswer!=answer:
	playerAnswer=input("Guess: ")
	playerAnswer=int(playerAnswer)
	tries=tries+1
	if playerAnswer<answer:
		taunt=random.randint(0,5)
		match taunt:
			case 0:
				print("When I say higher, I mean higher. Pass the joint.")
			case 1:
				print("What do you and your number have in common? You're both too short.")
			case 2:
				print("Is that the highest number you can think of? Because if so, you're in trouble.")
			case 3:
				print("Try getting in an airplane, maybe that'll help.")
			case 4:
				print("That number is as low as your chance of finding love.")
			case 5:
				print("Are you Gorb? Because you should ascend")
	if playerAnswer>answer:
		taunt=random.randint(0,5)
		match taunt:
			case 0:
				print("If you are in a building, find a window and jump out. Then you'll die and you'll be closer to your number, it's a win-win.")
			case 1:
				print("Make like an avatar of The Buried and GET LOWER!!!!")
			case 2:
				print("Go to hell. (You might find the number there)")
			case 3:
				print("Are you in a gun fight? Because GET DOWN!!!")
			case 4:
				print("You're saying numbers that match your overinflated ego, when you should be saying numbers that match your IQ")
			case 5:
				print("If the answer was an average forehead, your guess would be your forehead.")
print("Wow. You did it. You found the number. It only took you",tries,"tries. Congrats.")