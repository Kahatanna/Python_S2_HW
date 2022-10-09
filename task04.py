# Реализуйте алгоритм перемешивания списка,
# без использования встроеных методов (особенно SHUFFLE, без него)
# можно (нужно) использовать библиотеку Random

import random

def enterInt():
    while True:
        try:
            num = int(input('Введите количество элементов списка: '))
            return num
        except:
            print('Необходимо ввести ЦЕЛОЕ число. Попробуйте еще раз.')

n = enterInt()

listStart = []
listFinish = []

for i in range(1, n + 1):
    listStart.append(i)
print(listStart)

for i in range(len(listStart)):
    position = random.randint(0, len(listStart) - 1)
    listFinish.append(listStart.pop(position))
print(listFinish)