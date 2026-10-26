import random
deck=["Strike","Strike","Strike","Strike","Defend","Defend","Defend","Defend","Inflame","Footwork"]
otherCards=[]
hand=[]
enemyDifficulty=4
playingGame="yup"
playerHP=100
enemyChoices=["attack","block","buff"]
while playingGame=="yup":
	enemyHP=int(enemyDifficulty)*10+random.randint(int(enemyDifficulty)*3*-1,int(enemyDifficulty)*3)
	enemyStrength=0
	enemyDex=0
	playerStrength=0
	playerDex=0
	enemyBlock=0
	playerBlock=0
	enemyAttacking=0
	playerAttacking=0
	while enemyHP>0:
		print("Enemy HP:",enemyHP,"\nYour HP:",playerHP,"\nYour Dex:", playerDex,"\nYour Str:",playerStrength,"\n")
		hand=random.sample(deck,5)
		energy=3
		playerBlock=0
		enemyIntent=random.sample(enemyChoices,2)
		for thing in enemyIntent:
			if thing=="attack":
				enemyAttacking=enemyDifficulty*3+random.randint(enemyDifficulty*-1,enemyDifficulty)+enemyStrength
				print("enemy is attacking for",enemyAttacking)
			if thing=="block":
				enemyBlock+=enemyDifficulty*2+random.randint(enemyDifficulty*-1,enemyDifficulty)+enemyDex
				print("enemy is blocking for",enemyBlock)
			if thing=="buff":
				enemyDex+=1
				enemyStrength+=1
				print("Enemy is buffing")
		while energy>0:
			print(hand)
			print("Energy:",energy)
			play=hand[int(input("What do you play?: "))-1]
			if play=="Strike":
				hand.remove(play)
				energy-=1
				playerAttacking+=6+playerStrength
			if play=="Defend":
				hand.remove(play)
				energy-=1
				playerBlock+=5+playerDex
			if play=="Inflame":
				hand.remove(play)
				energy-=1
				playerStrength+=2
			if play=="Footwork":
				hand.remove(play)
				energy-=1
				playerDex+=2
		print("\n")
		if playerAttacking>enemyBlock:
			print("you dealt",playerAttacking-enemyBlock,"damage")
			enemyHP=enemyHP-playerAttacking+enemyBlock
			if enemyHP<=0:
				enemyBlock=0
				playerBlock=0
				enemyAttacking=0
				playerAttacking=0
				continue
		else:
			print("you dealt 0 damage")
		if enemyAttacking>playerBlock:
			playerHP=playerHP-enemyAttacking+playerBlock
			print("you took",enemyAttacking-playerBlock,"damage")
			if playerHP<=0:
				print("you died. L.")
				playingGame="nope"
				break
		else:
			print("you took 0 damage")
		enemyBlock=0
		playerBlock=0
		enemyAttacking=0
		playerAttacking=0
		print("\n")
	enemyDifficulty+=1
	print("You killed it ):")
