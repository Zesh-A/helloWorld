gameOver="false"
turn="X's turn: "
a1="_"
a2="_"
a3="_"
b1="_"
b2="_"
b3="_"
c1=" "
c2=" "
c3=" "
ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
while gameOver=="false":
	move=input(turn)
	match move:
		case "a1":
			if a1=="_":
				if turn=="X's turn: ":
					a1="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					a1="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "a2":
			if a2=="_":
				if turn=="X's turn: ":
					a2="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					a2="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "a3":
			if a3=="_":
				if turn=="X's turn: ":
					a3="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					a3="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "b1":
			if b1=="_":
				if turn=="X's turn: ":
					b1="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					b1="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "b2":
			if b2=="_":
				if turn=="X's turn: ":
					b2="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					b2="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "b3":
			if b3=="_":
				if turn=="X's turn: ":
					b3="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					b3="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "c1":
			if c1==" ":
				if turn=="X's turn: ":
					c1="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					c1="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "c2":
			if c2==" ":
				if turn=="X's turn: ":
					c2="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					c2="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case "c3":
			if c3==" ":
				if turn=="X's turn: ":
					c3="X"
					turn="O's turn: "
				elif turn=="O's turn: ":
					c3="O"
					turn="X's turn: "
				ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n "+c1+" | "+c2+" | "+c3
				print(ticTacToeBoard)
			else:
				print("That's already been played")
			if a1=="X" and a2=="X" and a3=="X":
				gameOver="true"
			if b1=="X" and b2=="X" and b3=="X":
				gameOver="true"
			if c1=="X" and c2=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b1=="X" and c1=="X":
				gameOver="true"
			if a2=="X" and b2=="X" and c2=="X":
				gameOver="true"
			if a3=="X" and b3=="X" and c3=="X":
				gameOver="true"
			if a1=="X" and b2=="X" and c3=="X":
				gameOver="true"
			if a3=="X" and b2=="X" and c1=="X":
				gameOver="true"
			if a1=="O" and a2=="O" and a3=="O":
				gameOver="true"
			if b1=="O" and b2=="O" and b3=="O":
				gameOver="true"
			if c1=="O" and c2=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b1=="O" and c1=="O":
				gameOver="true"
			if a2=="O" and b2=="O" and c2=="O":
				gameOver="true"
			if a3=="O" and b3=="O" and c3=="O":
				gameOver="true"
			if a1=="O" and b2=="O" and c3=="O":
				gameOver="true"
			if a3=="O" and b2=="O" and c1=="O":
				gameOver="true"
		case _:
			gameOver="true"
print("GGz")



