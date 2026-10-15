words=1
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
fileName=input("File: ")
with open(fileName) as fileContents:
	listedFileContents=list(fileContents.read())
for anything in listedFileContents:
	if anything==" " or anything=="\n":
		words=words+1
	else:
		match anything:
			case "a":
				a=a+1
			case "b":
				b=b+1
			case "c":
				c=c+1
			case "d":
				d=d+1
			case "e":
				e=e+1
			case "f":
				f=f+1
			case "g":
				g=g+1
			case "h":
				h=h+1
			case "i":
				i=i+1
			case "j":
				j=j+1
			case "k":
				k=k+1
			case "l":
				l=l+1
			case "m":
				m=m+1
			case "n":
				n=n+1
			case "o":
				o=o+1
			case "p":
				p=p+1
			case "q":
				q=q+1
			case "r":
				r=r+1
			case "s":
				s=s+1
			case "t":
				t=t+1
			case "u":
				u=u+1
			case "v":
				v=v+1
			case "w":
				w=w+1
			case "x":
				x=x+1
			case "y":
				y=y+1
			case "z":
				z=z+1







print("Words:",words,"\n","Letters:",a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)