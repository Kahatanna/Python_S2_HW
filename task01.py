# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11

def enterFloat():
    while True:
        try:
            num = float(input('Введите вещественное число: '))
            return num
        except:
            print('Необходимо ввести ВЕЩЕСТВЕННОЕ число. Разделитель - точка. Попробуйте еще раз.')

num = enterFloat()
sum = 0

for i in str(num):
    if i.isdigit():
        sum+=int(i)
print('Сумма цифр числа {} равна {}'.format(num, sum))