total=0
sortedList=[]
intOnlyList=[]
x="hi"
for thing in input("What numbers?: ").split():
	try:
		thing=int(thing)
		intOnlyList.append(thing)
	except ValueError:
		pass
while len(intOnlyList)>0:
	for thing in intOnlyList:
		if x=="hi":
			x=thing
		else:
			if thing<int(x):
				x=thing
	if x!="hi":
		total=total+int(x)
		sortedList.append(int(x))
		intOnlyList.remove(int(x))
		x="hi"
print(sortedList,"\nmean:",total/int(len(sortedList)),"\nmedian:",sortedList[int(len(sortedList))//2])