class Pupils:
	head = True
	legs = 2
	fingers = 10
	marks = "ДВАААА!!!!"
	write = True
	read = True
	def learn(self):
		if self.head == True:
			print("А голову ты дома не забыл?!")
		else:
			print(self.marks)
suleyman = Pupils()
print(suleyman.marks)
suleyman.learn()

