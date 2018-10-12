print("Welcome to FP")
def f1(a,b):
	print("Entering f1")
	print("a=",a)
	print("b=",b)
	def f2(m,n):
		print("m=",m)
		print("n=",n)
	a=a+10
	b=b+20
	print("a=",a)
	c=3+a
	print("b=",b)

	d=2+b
	print("c=",c)
	print("d=",d)
	
	f2(11,12)
	print("a=",a)
	print("b=",b)
	print("Leaving f1")
f1(5,10)

