notANumber=0
x="hi"
highOrLow=input("Do you want the highest or lowest?: ")
theListUnlisted=input("What numbers?: ")
theList=theListUnlisted.split()
for thing in theList:
	try:
		thing=int(thing)
		if x=="hi":
			x=thing
		if highOrLow=="highest":
			if thing>x:
				x=thing
		elif highOrLow=="lowest":
			if thing<x:
				x=thing
		else:
			print("Fuck you you didn't say highest or lowest")
	except ValueError:
		notANumber=notANumber+1
print("The number is",x)
if notANumber!=0:
	print("btw you said",notANumber,"things that aren't numbers")