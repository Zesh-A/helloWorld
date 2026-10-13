import random
number="1"
number=int(number)
playerCorrect="true"
while playerCorrect=="true":
	playerInput=input("Number: ")
	playerInput=int(playerInput)
	if playerInput==number:
		number=number+1
		if playerInput==10:
			print("Wow, you can count to 10. Congrats.")
		else:
			successWords=random.randint(1,5)
			match successWords:
				case 1:
					print("Wow, you know how to count.")
				case 2:
					print("Yup,",playerInput,"is correct")
				case 3:
					print("Y'know that's kinda impressive, if you're a toddler.")
				case 4:
					print("You may have gotten this far, but i'm sure the next number will stump you!")
				case 5:
					print("Uhuh")
	else:
		failureWords=random.randint(1,5)
		match failureWords:
			case 1:
				print("Dude you can't count? That not surprising actually.")
			case 2:
				print("You failed. On",number-1,". How?")
			case 3:
				print("This isn't supposed to be a guessing game you know")
			case 4:
				print("That's my bad actually, I expected too much from you.")
			case 5:
				print("What do they teach in school these days?")
		tryAgain=input("Try again?: ")
		if tryAgain=="no":
			playerCorrect="false"
		number=1
print("Later loser")