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
print(answer)
