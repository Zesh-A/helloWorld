import time
import random
totalTime=0
tryAgain="y"
while tryAgain=="y":
	for _ in range(5):
		input("Ready?")
		time.sleep(random.randint(1,10))
		startTime=time.time()
		input("Now")
		endTime=time.time()
		thisTime=float(endTime)-float(startTime)
		if thisTime==0:
			print("You went too fast")
			break
		else:
			print(thisTime)
			totalTime=totalTime+thisTime
	if thisTime!=0:
		print("Average:",round(totalTime/5,3),"seconds")
	tryAgain=input("Try again? (y/n):")
	totalTime=0
