import random

number1 = int(input("Введите первое число: "))
number2 = random.randint(0, 10)
answer = int(input("Скажи результат умножения " \
    + str(number1) + " на " + str(number2) + ": "))
if answer == number1 * number2:
    print("Молодца, держи косточку")
else:
    print("Останешься без косточки!!")
    print("Правильный ответ: " + str(number1 * number2))
