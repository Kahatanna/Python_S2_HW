# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def enterInt():
    while True:
        try:
            num = int(input('Введите N количество элементов списка [-N, N]: '))
            return num
        except:
            print('Необходимо ввести ЦЕЛОЕ число. Попробуйте еще раз.')

n = enterInt()
list = [0]

for i in range(1, n + 1):
    list.append(i)
    list.insert(0, -i)
print(list)

with open('pos.txt', 'r') as file:
    pos1 = int(file.readline()[:-1])
    pos2 = int(file.readline())

print('Произведение {}-го и {}-го элементов = {}'.format(pos1, pos2, int(list[pos1])*int(list[pos2])))