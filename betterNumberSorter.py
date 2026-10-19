notANumber=0
y=0
sortedList=[]
x="hi"
theListUnlisted=input("What numbers?: ")
theList=theListUnlisted.split()
while y<100:
	for thing in theList:
		try:
			thing=int(thing)
		except ValueError:
			theList.remove(thing)
			break
	y+=1
while len(theList)>0:
	for thing in theList:
		thing=int(thing)
		if x=="hi":
			x=thing
		else:
			try:
				if thing<x:
					x=thing
			except TypeError:
				pass
	x=str(x)
	sortedList.append(x)
	print(x)
	theList.remove(x)
	x="hi"
print(sortedList)
if notANumber!=0:
	print("btw you said",notANumber,"things that aren't numbers")