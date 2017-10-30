class Circle:
	def __init__(self, radius):
		self.radius = radius

	# def get_area(self):
	# 	return self.radius ** 2 * 3.14

	# def set_area(self, value):
	# 	pass

	# area = property(get_area, set_area)

	@property
	def area(self):
		return self.radius ** 2 * 3.14

	# @area.setter
	# def area(self, value):
	# 	pass



my_circle = Circle(5)
print(my_circle.area)
my_circle.radius = 10
print(my_circle.area)