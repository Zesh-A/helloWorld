option="y'know it dosen't really matter"
while option!="3":
	option=input("Press 1 to add, press 2 to show, press 3 to end: ")
	if option=="1":
		with open ("toDoList", "a") as toDoList:
			toDoList.write(input("What do you need to do?: "))
			toDoList.write("\n")
	elif option=="2":
		with open ("toDoList", "r") as toDoList:
			print(toDoList.read())
	elif option=="3":
		print("later loser")
	else:
		print("Get good loser lol")
