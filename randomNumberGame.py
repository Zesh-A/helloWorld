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
	if playerAnswer!=answer:
		taunt=random.randint(0,5)
		match taunt:
			case 0:
				print("Not even close")
			case 1:
				print("Are you even trying?")
			case 2:
				print("You're like, really bad at this")
			case 3:
				print("Buddy. No.")
			case 4:
				print("I hate to tell you this, but that's not quite right")
			case 5:
				print("Get Good")
print("Wow. You did it. You found the number. It only took you",tries," tries. Congrats.")