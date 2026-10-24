total=0
sortedList=[]
intOnlyList=[]
x="hi"
for thing in input("What numbers?: ").split():
	try:
		thing=float(thing)
		intOnlyList.append(thing)
	except ValueError:
		print("dropping " + thing + " from dataset, get good.")
while len(intOnlyList)>0:
	for thing in intOnlyList:
		if x=="hi":
			x=thing
		else:
			if thing<float(x):
				x=thing
	if x!="hi":
		total=total+float(x)
		sortedList.append(float(x))
		intOnlyList.remove(float(x))
		x="hi"
print(sortedList,"\nmean:",total/float(len(sortedList)),"\nmedian:",sortedList[int(len(sortedList))//2])