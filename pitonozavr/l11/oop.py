class Cars:
	wheels = 4
	engine = True

	def ride(self):
		print("TRRRRRR!!")

volga = Cars()

# print(volga)
# print(volga.wheels)
print(volga.engine)
volga.ride()

volga.wheels += 6
print(volga.wheels)
