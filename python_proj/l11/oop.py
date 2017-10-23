class A:
	x = 2
	y = 3
	def summ(self,x,y):
		return x + y 

a = A()
b = A()
x = 150
y = 100
a.x = 5
a.y = 6
print(a.summ(a.x,a.y)," -- ", b.summ(x,y))
		