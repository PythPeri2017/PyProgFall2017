import random # подключили библиотеку random

print("Реши пример!!!")
number1 = int(input("Введи первое число: "))
number2 = random.randint(0, 10) # случайное число от 0 до 10
answer = int(input("Умножь " + str(number1) \
    + " на " + str(number2) + " : "))

if (answer == number1 * number2):
    print("МужиГ!!")
    print("Гордость нации!")
else:
    print("Позор, стыд, расстрел!!!!")
