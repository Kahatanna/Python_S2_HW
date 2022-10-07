# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

def enterInt():
    while True:
        try:
            num = int(input('Введите целое число: '))
            return num
        except:
            print('Необходимо ввести ЦЕЛОЕ число. Попробуйте еще раз.')

def Factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * Factorial(n-1)
num = enterInt()
list = []

for i in range(1, num + 1):
    list.append(Factorial(i))
print(list)