# scientists = ("Альберт", "Максвелл", "Диофант") # кортеж
# main = "Cobol"
# langs = "Java", "Assembler", "Scratch", main
# print(langs)
# print(langs[1])
# x, y, z = scientists
# print(x, y, z)
# a, b, c, d, e = 1, 2, 3, 4, 5
# print(a, b, c)
a = 4
b = 8
a, b = b, a

saeed = {}
print(saeed)
writers = {"Рэй Бредбери", "Джордж Оруэлл", \
"Жуль Верн", "Джордж Мартин", "Эрих Мария Ремарк", "Джордж Оруэлл"}
print(writers)
antiutop = {"Оксана", "Рэй Бредбери", "Джордж Оруэлл", "Замятин"}
print(writers & antiutop) # пересечение
print(writers | antiutop) # объединение
print(writers - antiutop) # вычитание 2 из 1
print(antiutop - writers) # вычитание 1 из 2
print(writers ^ antiutop) # все элементы без общих

directors = {
	"Спилберг": ("Парк Юрского Периода", "Челюсти", "Список Шиндлера"),
	"Нолан": ("Дюнкек", "Престиж", "Начало"),
	"Бондарчук": ("Притяжение", "9 рота", "Обитаемый остров")
}
# print(directors["Нолан"])
directors["Бондарчук"] = ["Мусор", "Шлак"]
# print(directors)
directors[5] = 12345
directors[True] = "Матильда"
print(directors)
directors[("Билл Гейтс", "Марк Цукербрин")] = "Айтишки"
print(directors["Билл Гейтс"])
