keepGoing="y"
while keepGoing=="y":
	number=input("number: ") 
	operation=input("operation: ")
	numberTwo=input("second number: ")
	number=int(number)
	numberTwo=int(numberTwo)
	match operation:
		case "+":
			answer=number+numberTwo
		case "-":
			answer=number-numberTwo
		case "*":
			answer=number*numberTwo
		case "/":
			answer=number/numberTwo
		case _:
			answer="that's not a fucking operation, get good"
	if answer==67:
		print("Nice try")
	elif answer==69:
		print("Nope")
	elif answer==3.14:
		print("Whoa nice")
	elif answer==42:
		print("That's the answer")
	else:
		print(answer)

	keepGoing=input("keep going? (y/n): ")
else:
	print("Bye")
