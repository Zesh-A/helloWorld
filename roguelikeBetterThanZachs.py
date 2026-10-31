import random
def playCard(hand, discardPile, nameOfCard, energyCost):
	global energy
	energy-=energyCost
	hand.remove(nameOfCard)
	discardPile.append(nameOfCard)
discardPile=[]
relics=["Vajra", "Oddly Smooth Stone", "Ice Cream", "Mercury Hourglass", "Orichalcum", "Cloak Clasp", "Parrying Shield", "Gorget", "Happy Flower", "Lantern", "Candelabra", "Chandelier", "Blood Vial", "Lee's Waffel", "Bread"]
relicsOwned=[]
deck=["Strike","Strike","Strike","Strike","Defend","Defend","Defend","Defend","Inflame","Footwork"]
otherCards=["Iron Wave", "Wisp","Friendship","The Scythe","Celestial Might","Dagger Spray", "Dash", "Blood Wall", "Fight Me", "Bludgeon", "Bloodletting","Not Yet", "Claw", "Leap"]
hand=[]
enemyDifficulty=4
playingGame="yup"
playerHP=100
playerMaxHP=100
scytheDamage=0
scytheRemoved="false"
enemyChoices=["attack","block","buff"]
flowey=0
plating=0
extraEnergy=0
paths=["Elite","Campfire","Chest"]
room=0
isItElite="No"
while playingGame=="yup":
	room+=1
	howManyOptions=random.randint(0,4)
	if howManyOptions==3 or howManyOptions==4:
		howManyOptions=0
	pathOptions=random.sample(paths,random.randint(0,2))
	pathOptions.append("Normal")
	print(pathOptions)
	nextRoom=pathOptions[int(input("Which way?"))-1]
	if nextRoom=="Normal":
		pass
	elif nextRoom=="Chest":
		relicGained=random.sample(relics,1)[0]
		relicsOwned.append(relicGained)
		relics.remove(relicGained)
		if relicGained=="Lee's Waffel":
			playerMaxHP+=7
			playerHP=playerMaxHP
		if relicGained=="Bread":
			extraEnergy=1
		print("Your relics:",relicsOwned)
		continue
	elif nextRoom=="Campfire":
		playerHP=playerMaxHP
		continue
	elif nextRoom=="Elite":
		isItElite="Yes"
	enemyHP=int(enemyDifficulty)*10+random.randint(int(enemyDifficulty)*2*-1,int(enemyDifficulty)*2)
	if isItElite=="Yes":
		enemyHP*=2
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
	turn=0
	if "Gorget" in relicsOwned:
		plating=4
	if "Blood Vial" in relicsOwned:
		playerHP+=2
	if "Vajra" in relicsOwned:
		playerStrength+=1
	if "Oddly Smooth Stone" in relicsOwned:
		playerDex+=1
	if playerHP>playerMaxHP:
		playerHP=playerMaxHP
	while enemyHP>0:
		print("Enemy HP:",enemyHP,"\nYour HP:",playerHP,"\nYour Dex:", playerDex,"\nYour Str:",playerStrength,"\n")
		for cardDraw in range(0,5):
			if len(deck)==0:
				for discardedCard in discardPile:
					deck.append(discardedCard)
				discardPile.clear()
			cardDrawn=random.sample(deck,1)[0]
			hand.append(cardDrawn)
			deck.remove(cardDrawn)
		if "Ice Cream" in relicsOwned:
			energy+=3+isFriend+extraEnergy
		else:
			energy=3+isFriend+extraEnergy
		if turn==0:
			if "Lantern" in relicsOwned:
				energy+=1
			if "Bread" in relicsOwned:
				energy-=3
		if turn==1:
			if "Candelabra" in relicsOwned:
				energy+=2
		if turn==2:
			if "Chandelier" in relicsOwned:
				energy+=3
		if "Happy Flower" in relicsOwned:
			flowey+=1
			if flowey==2:
				flowey=0
				energy+=1
		turn+=1
		playerBlock=0
		enemyIntent=random.sample(enemyChoices,2)
		for thing in enemyIntent:
			if thing=="attack":
				enemyAttacking=enemyDifficulty*3+random.randint(enemyDifficulty*-1,enemyDifficulty)+enemyStrength
				if isItElite=="Yes":
					enemyAttacking=round(enemyAttacking*1.3)
				print("enemy is attacking for",enemyAttacking)
			if thing=="block":
				enemyBlock+=enemyDifficulty*2+random.randint(enemyDifficulty*-1,enemyDifficulty)+enemyDex
				if isItElite=="Yes":
					enemyBlock=round(enemyBlock*1.3)
				print("enemy is blocking for",enemyBlock)
			if thing=="buff":
				enemyDex+=1
				enemyStrength+=1
				if isItElite=="Yes":
					enemyDex+=1
					enemyStrength+=1
				print("Enemy is buffing")
		while energy>-1:
			print(hand)
			print("Energy:",energy)
			try:
				play=hand[int(input("What do you play?: "))-1]
			except ValueError:
				print("we'll take that as an end turn!")
				break
			if play=="Strike":
				if energy>0:
					playCard(hand, discardPile, play, 1)
					playerAttacking+=6+playerStrength
				else:
					print("You don't have enough energy")
			if play=="Defend":
				if energy>0:
					playCard(hand, discardPile, play, 1)		
					playerBlock+=5+playerDex
				else:
					print("You don't have enough energy")
			if play=="Inflame":
				if energy>0:
					playCard(hand, discardPile, play, 1)
					playerStrength+=2
				else:
					print("You don't have enough energy")
			if play=="Footwork":
				if energy>0:
					playCard(hand, discardPile, play, 1)
					playerDex+=2
				else:
					print("You don't have enough energy")
			if play=="Iron Wave":
				if energy>0:
					playerBlock+=5+playerDex
					playerAttacking+=5+playerStrength
					playCard(hand, discardPile, play, 1)
				else:
					print("You don't have enough energy")
			if play=="Wisp":
				playCard(hand, discardPile, play, 0)
				energy+=1
			if play=="Friendship":
				if energy>0:
					playCard(hand, discardPile, play, 1)
					isFriend+=1
					playerStrength-=2
				else:
					print("You don't have enough energy")
			if play=="The Scythe":
				if energy>1:
					playCard(hand, discardPile, play, 2)
					discardPile.remove(play)
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
				if energy>0:
					playCard(hand, discardPile, play, 1)
					playerAttacking+=4+playerStrength
					playerAttacking+=4+playerStrength
				else:
					print("You don't have enough energy")
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
					if playerHP>playerMaxHP:
						playerHP=playerMaxHP
				else:
					print("You don't have enough energy")
			if play=="Claw":
				playCard(hand, discardPile, play, 0)
				playerAttacking+=3+playerStrength+clawsPlayed
				clawsPlayed+=2
			if play=="Leap":
				if energy>0:
					playerBlock+=9+playerDex
					playCard(hand, discardPile, play, 1)
				else:
					print("You don't have enough energy")
		if "Orichalcum" in relicsOwned:
			if playerBlock==0:
				playerBlock=6
		if "Cloak Clasp" in relicsOwned:
			for card in hand:
				playerBlock+=1
		if plating>0:
			playerBlock+=plating
			plating-=1
		if "Mercury Hourglass" in relicsOwned:
			playerAttacking+=3
		if "Parrying Shield" in relicsOwned:
			if playerBlock>=10:
				playerAttacking+=6
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
	if playingGame=="nope":
		break
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
	if isItElite=="Yes":
		relicGained=random.sample(relics,1)[0]
		relicsOwned.append(relicGained)
		relics.remove(relicGained)
		if relicGained=="Lee's Waffel":
			playerMaxHP+=7
			playerHP=playerMaxHP
		if relicGained=="Bread":
			extraEnergy=1
		isItElite="No"
	print("Your Relics: ",relicsOwned, "\nYour health:", playerHP, "\nYour deck:", deck)
	pathOptions=random.sample(paths,random.randint(0,2))
	pathOptions.append("Normal")
	print(pathOptions)
	nextRoom=pathOptions[int(input("Which way?"))-1]
