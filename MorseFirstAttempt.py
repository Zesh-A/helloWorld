output=[]
morse={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."," ":"/"}
input=input("Good Morning: ")
listedInput=list(input)
for thing in listedInput:
	thing=morse[thing]
	output.append(thing)
	output.append(" ")
finishedThing="".join(output)
print(finishedThing)