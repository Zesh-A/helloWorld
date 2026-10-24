listOfInts=input("Numbers: ").split()
print(listOfInts)
listOfInts=list(map(int,listOfInts))
targetNumber=int(input("Target number: "))
for numberOne in listOfInts:
	for numberTwo in listOfInts:
		if numberOne+numberTwo==targetNumber:
			firstNumberPosition=listOfInts.index(numberOne)
			secondNumberPosition=listOfInts.index(numberTwo)
try:
	print(firstNumberPosition+1,secondNumberPosition+1)
except NameError:
	print("couldn't find a match")