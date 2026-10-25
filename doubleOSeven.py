import random
playerAmmo=0
computerAmmo=0
bothHaveAmmo=["load","block","block","shoot","shoot"]
playerHasAmmo=["load","block"]
computerHasAmmo=["shoot","load"]
alive="yes"
while alive=="yes":
	playerMove=input("load, shoot, or block: ")
	if playerMove in ("load","shoot","block"):
		if playerMove=="shoot" and playerAmmo==0:
			print("You don't have ammo")
			continue
		if playerAmmo==0 and computerAmmo==0:
			computerMove="load"
		elif playerAmmo!=0 and computerAmmo!=0:
			computerMove=bothHaveAmmo[random.randint(0, 4)]
		elif playerAmmo!=0 and computerAmmo==0:
			computerMove=playerHasAmmo[random.randint(0, 1)]
		elif playerAmmo==0 and computerAmmo!=0:
			computerMove=computerHasAmmo[random.randint(0, 1)]
		if playerMove=="shoot" and computerMove=="load":
			alive="no"
			winner="player"
		if playerMove=="load" and computerMove=="shoot":
			alive="no"
			winner="computer"
		if playerMove=="load":
			playerAmmo+=1
		if computerMove=="load":
			computerAmmo+=1
		if playerMove=="shoot":
			playerAmmo-=1
		if computerMove=="shoot":
			computerAmmo-=1
		print("Computer's move:",computerMove,"\nPlayer's ammo:",playerAmmo,"\nComputer's ammo:",computerAmmo)
	else:
		print("you didn't say load shoot or block")
print("Winner:",winner)