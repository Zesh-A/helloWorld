listOfInts=input("Numbers: ").split()
listOfInts=list(map(int,listOfInts))
targetNumber=int(input("Target number: "))
for numberOne in listOfInts:
	for numberTwo in listOfInts:
		if numberOne!=numberTwo:
			for operation in ["+","-","*","/"]:
				match operation:
					case "+":
						answer=numberOne+numberTwo
					case "-":
						answer=numberOne-numberTwo
					case "*":
						answer=numberOne*numberTwo
					case "/":
						answer=numberOne/numberTwo
				if answer==targetNumber:
					correctFirstNumber=numberOne
					correctSecondNumber=numberTwo
					operationAnswer=operation
try:
	print(correctFirstNumber,operationAnswer,correctSecondNumber)
except NameError:
	print("couldn't find a match")