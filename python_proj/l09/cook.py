# Получить все продукты в холодильнике
# Перебрать и приготовить
# Дать название нашему блюду - взять первые 
# 	буквы ингридиентов

import random

def my_cook(*args, major = "мазик"):
	for product in args:
		making_food(product)
	print("Обильно нальем сверху " + major)
	print("Наше блюдо - " + food_name(args) + " - готово!")

def making_food(ingridient):
	print(random.choice(cook_variants) + " " +
		ingridient)

def food_name(ingridients):
	name = ""
	for ing in ingridients:
		name += ing[1]
	return name


cook_variants = ["Пожарим", "Сварим", 
	"Разгоним", "Похороним"]

my_cook("яйца", "молоко", "процессор", "труп кошки",
	"корм для кошки")