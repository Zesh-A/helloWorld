import random
def playCard(hand, discardPile, nameOfCard, energyCost):
	global energy
	energy-=energyCost
	hand.remove(nameOfCard)
	discardPile.append(nameOfCard)
discardPile=[]
deck=["Strike","Strike","Strike","Strike","Defend","Defend","Defend","Defend","Inflame","Footwork"]
otherCards=["Iron Wave", "Wisp","Friendship","The Scythe","Celestial Might","Dagger Spray", "Dash", "Blood Wall", "Fight Me", "Bludgeon", "Bloodletting","Not Yet", "Claw", "Leap"]
hand=[]
enemyDifficulty=4
playingGame="yup"
playerHP=100
scytheDamage=0
scytheRemoved="false"
enemyChoices=["attack","block","buff"]
while playingGame=="yup":
	enemyHP=int(enemyDifficulty)*10+random.randint(int(enemyDifficulty)*2*-1,int(enemyDifficulty)*2)
	enemyStrength=0
	enemyDex=0
	playerStrength=0
	playerDex=0
	enemyBlock=0
	playerBlock=0
	enemyAttacking=0
	playerAttacking=0
	isFriend=0
	clawsPlayed=0
	while enemyHP>0:
		print("Enemy HP:",enemyHP,"\nYour HP:",playerHP,"\nYour Dex:", playerDex,"\nYour Str:",playerStrength,"\n")
		for cardDraw in range(0,5):
			if len(deck)==0:
				print(discardPile)
				for discardedCard in discardPile:
					deck.append(discardedCard)
				print(deck)
				discardPile.clear()
				print(deck)
			cardDrawn=random.sample(deck,1)[0]
			hand.append(cardDrawn)
			print(cardDrawn)
			print(deck)
			deck.remove(cardDrawn)
		energy=3+isFriend
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
				playCard(hand, discardPile, play, 1)
				playerAttacking+=6+playerStrength
			if play=="Defend":
				playCard(hand, discardPile, play, 1)		
				playerBlock+=5+playerDex
			if play=="Inflame":
				playCard(hand, discardPile, play, 1)
				playerStrength+=2
			if play=="Footwork":
				playCard(hand, discardPile, play, 1)
				playerDex+=2
			if play=="Iron Wave":
				playerBlock+=5+playerDex
				playerAttacking+=5+playerStrength
				playCard(hand, discardPile, play, 1)
			if play=="Wisp":
				playCard(hand, discardPile, play, 0)
				energy+=1
			if play=="Friendship":
				playCard(hand, discardPile, play, 1)
				isFriend+=1
				playerStrength-=2
			if play=="The Scythe":
				if energy>1:
					playCard(hand, discardPile, play, 2)
					deck.remove(play)
					scytheRemoved="True"
					playerAttacking+=13+playerStrength+scytheDamage
					scytheDamage+=5
				else:
					print("You don't have enough energy")
			if play=="Celestial Might":
				if energy>1:
					playCard(hand, discardPile, play, 2)
					playerAttacking+=6+playerStrength
					playerAttacking+=6+playerStrength
					playerAttacking+=6+playerStrength
				else:
					print("You don't have enough energy")
			if play=="Dagger Spray":
				playCard(hand, discardPile, play, 1)
				playerAttacking+=4+playerStrength
				playerAttacking+=4+playerStrength
			if play=="Dash":
				if energy>1:
					playCard(hand, discardPile, play, 2)
					playerAttacking+=10+playerStrength
					playerBlock+=10+playerDex
				else:
					print("You don't have enough energy")
			if play=="Blood Wall":
				if energy>1:
					playCard(hand, discardPile, play, 2)
					playerHP-=2
					playerBlock+=16+playerDex
				else:
					print("You dont have enough energy")
			if play=="Fight Me":
				if energy>1:
					playCard(hand, discardPile, play, 2)
					playerAttacking+=5+playerStrength
					playerAttacking+=5+playerStrength
					playerStrength+=3
					enemyStrength+=1
				else:
					print("You don't have enough energy")
			if play=="Bludgeon":
				if energy>2:
					playCard(hand, discardPile, play, 3)
					playerAttacking+=32+playerStrength
			if play=="Bloodletting":
				playCard(hand, discardPile, play, 0)
				playerHP-=3
				energy+=2
			if play=="Not Yet":
				if energy>1:
					playCard(hand, discardPile, play, 2)
					playerHP+=10
				else:
					print("You don't have enough energy")
			if play=="Claw":
				playCard(hand, discardPile, play, 0)
				playerAttacking+=3+playerStrength+clawsPlayed
				clawsPlayed+=2
			if play=="Leap":
				playerBlock+=9+playerDex
				playCard(hand, discardPile, play, 1)
		print("\n")
		if playerAttacking>enemyBlock:
			print("you dealt",playerAttacking-enemyBlock,"damage")
			enemyHP=enemyHP-playerAttacking+enemyBlock
			if enemyHP<=0:
				enemyBlock=0
				playerBlock=0
				enemyAttacking=0
				playerAttacking=0
				for cardUnplayed in hand:
					discardPile.append(cardUnplayed)
				hand.clear()
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
		for cardUnplayed in hand:
			discardPile.append(cardUnplayed)
		hand.clear()
	enemyDifficulty+=1
	print("You killed it ):\n")
	for thingy in discardPile:
		deck.append(thingy)
	discardPile.clear()
	cardChoices=random.sample(otherCards,3)
	print(cardChoices)
	cardChoosen=(cardChoices[int(input("Which do you want?: "))-1])
	deck.append(cardChoosen)
	if cardChoosen=="The Scythe":
		otherCards.remove("The Scythe")
	if scytheRemoved=="True":
		deck.append("The Scythe")
		scytheRemoved="false"
