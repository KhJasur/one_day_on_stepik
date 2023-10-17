
#print('how are you?','where are you?')# здесь "," работает как пробел

'''print('Как тебя зовут?')# Чтобы сделать многострочный коментарий нужно ввести одинарные ковычки
name=input()#команда input работает для ввода данных с экрана
print(" Привет меня зовут",name)'''

'''print('a','b', end='@')
#print()
print(' ','a','b','c','d', sep='**')'''

#print()

'''print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='#')
print('m', 'n', 'o', sep='/', end='!')'''

'''print('Python', end='\n\n\n')
print("huli kod ne rabotayet?")'''

'''print('Mercury', 'Venus', sep='*', end='!')
print('Mars', 'Jupiter', sep='**', end='?')'''

'''print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')'''



'''gay = input()
gachi = input()
muchi = input()
muchi2 = input()
print(gachi, muchi, muchi2, sep=gay)'''


'''name,surname = 'Jasur', 'Hashimov' #Это просто прикол 
print('Imya:',name, "Familiya:", surname)'''

'''name, surname = input(), input()
print('Имя:', name, 'Фамилия:', surname)'''

'''name1 = 'Timur'
name2 = 'Gvido' #Так можно менять местами
name1, name2 = name2, name1 
print(name1, " ", name2)'''

# Интерпретатор- это программа, которая переводит напмсанный нами код в инструкции понятные компьютеру

# a = int(input()) # Переменую лучше писать с маленькой буквой, классы и писать с большой буквой
# b = a + 1
# print(b)
# c = b + 1
# print(c)
# d = c + 1
# print(d)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a + b + c)

# a = int(input())
# v = a * a * a
# print("Объем =", v)
# s = 6 * a * a
# print("Площадь полной поверхности =", s)


# def f(a, b):
#     return 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41
#
# a = int(input())
# b = int(input())
#
# result = f(a, b)
# print('f(', a, ', ', b, ') =', result)

# a = int(input())
# b = a + 1
# print("Следующее за числом", a, "число:", b)
# c = a - 1
# print("Для числа", a, "число: ", c)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# print(a * 3 + b * 3 + c * 3 + d * 3)

# a = int(input())
# b = int(input())
# print(a, '+', b, '=', a + b)
# print(a, '-', b, '=', a - b)
# print(a, '*', b ,'=', a * b)


# a1 = int(input())
# d = int(input())
# n = int(input())
# print(a1 + d * (n - 1))


# a = int(input())
# b = a * 2
# c = a * 3
# d = a * 4
# e = a * 5
# print(a, b, c, d, e, sep="---")

# b1 = int(input())
# q = int(input())
# n = int(input())
# print(b1 * q**(n - 1))


# uchenik = int(input())
# mandarin =int(input())
#
# print(mandarin // uchenik)
# print(mandarin % uchenik)


# a = int(input())
# b = (a + 3) // 4
# print(b)


# a = int(input())
# b = a // 60
# c = a % 60
# print(a, 'это', b, 'час', c, 'минут')

# n = int(input())
# a = (n // 10 ** 2) % 10
# b = (n // 10 ** 1) % 10
# c = (n // 10 ** 0) % 10
# print("Сумма цифр =", a + b + c)
# print("Произведение =", a * b * c)

# chislo = int(input())
# a1 = (chislo // 10 ** 2) % 10
# a2 = (chislo // 10 ** 1) % 10
# a3 = (chislo // 10 ** 0) % 10
# a = str(a1)
# b = str(a2)
# c = str(a3)
# print(chislo,
#       a + c + b,
#       b + a + c,
#       b + c + a,
#       c + a + b,
#       c + a + b,
#       sep='\n')



chislo = int(input())
a1 = (chislo // 10 ** 3) % 10
a2 = (chislo // 10 ** 2) % 10
a3 = (chislo // 10 ** 1) % 10
a4 = (chislo // 10 ** 0) % 10
a = str(a1)
b = str(a2)
c = str(a3)
d = str(a4)
print('Цифра в позиции тысяч равна', a)
print('Цифра в позиции сотен равна', b)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', d)



