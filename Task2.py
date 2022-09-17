# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# спроси у гугла:
# Как разложить число на простые множители
# Последовательность действий при разложении числа на простые множители:

# 1. Проверяем по таблице простых чисел, не является ли данное число простым.
# 2. Если нет, то последовательно подбираем самое маленькое простое число из таблицы простых чисел, на которое данное число делится без остатка, и выполняем деление.
# 3. Проверяем по таблице простых чисел, не является ли полученное частное простым числом.
# 4. Если нет, то последовательно подбираем самое маленькое простое число из таблицы простых чисел, на которое полученное частное делится нацело, и выполняем деление.
# 5. Повторяем пункты 3 и 4 до тех пор, пока в частном не получится единица.

# import sympy 
# у меня почему-то не загружается эта библиотека. Очень жаль.

file = 'tabl.txt'
sched = open(file, 'r')

n = int(input('Введите число N = '))

# sched = list(sympy.primerange(0, 100))

if int(n) < 0: n = -n
if int(n) > 1000: print('К сожалению, столько мы не умеем') # таблица простых чисел только до 1000

print(n, end = ' делится на ')
for line in sched:
    if n%int(line) == 0:
        print (int(line), end=', ')
        
# или

list = []
for line in sched:
    if n%int(line) == 0:
        list.append(int(line))

print(list)