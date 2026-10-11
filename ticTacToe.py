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
ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
while gameOver=="false":
	move=input(turn)
	match move:
		case "a1":
			if turn=="X's turn: ":
				a1="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				a1="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "a2":
			if turn=="X's turn: ":
				a2="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				a2="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "a3":
			if turn=="X's turn: ":
				a3="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				a3="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "b1":
			if turn=="X's turn: ":
				b1="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				b1="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "b2":
			if turn=="X's turn: ":
				b2="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				b2="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "b3":
			if turn=="X's turn: ":
				b3="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				b3="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "c1":
			if turn=="X's turn: ":
				c1="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				c1="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "c2":
			if turn=="X's turn: ":
				c2="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				c2="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)
		case "c3":
			if turn=="X's turn: ":
				c3="X"
				turn="O's turn: "
			elif turn=="O's turn: ":
				c3="O"
				turn="X's turn: "
			ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
			print(ticTacToeBoard)




ticTacToeBoard="_"+a1+"_|_"+a2+"_|_"+a3+"_\n_"+b1+"_|_"+b2+"_|_"+b3+"_\n  "+c1+"|"+c2+"  | "+c3
print(ticTacToeBoard)



