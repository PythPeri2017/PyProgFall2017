# Квадратное уравнение ax^2 + bx + c = 0.
# Найти дискриминант Д = b^2 - 4ac. Если Д > 0, то
# 	х1 = (-b + sqrt(Д))/2a
# 	x2 = (-b - sqrt(Д))/2a
# иначе если Д = 0, то
# 	x = -b /2a
# иначе
# 	действительных корней нет

def quadratic(a, b, c):

	disc = b ** 2 - 4 * a * c

	if disc > 0:
		x1 = (-b + disc ** 0.5) / (2 * a)
		x2 = (-b - disc ** 0.5) / (2 * a)
		return x1, x2

	elif disc == 0:
		x = -b / (2 * a)
		return x

	else:
		return "Действительных корней нет"

