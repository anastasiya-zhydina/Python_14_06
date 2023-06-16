#Создание виртуальной среды: python3 -m venv .folder --> ввести в новом терминале

# print("Введите первое число: ")
# a = int(input())
# b = int(input('введите второе число: '))
# print(f"Сумма чисел {a} и {b} равна {a+b}")

# c = 5.99
# print(c)
# print(type(c))
# n = int(c)
# print(n)
# print(type(n))

# a = 5.767764
# b = 5.676773
# print(round(a*b, 3))

# a = 1 < 4
# print(a)

# a = 1<4 and 5>2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1<3<5<10
# print(a)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# a = 123456789
# summa = 0
# while a>0:
#     x = a%10
#     summa += x
#     a //= 10
# print(summa)

#метод флажка, минимальный делитель целого числа

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n%i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i>n//2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# a = 'qwerty'
# print(a[4])

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ еще этих МяГкИх французких булок'
# print(len(text)) # позводяет узнать размер нашей строки
# print('еще' in text) # есть ли данная строка в тексте
# print(text.lower()) #переводит все буквы строки в нижний регистр
# print(text.upper()) #переводит все буквы в верхний регистр
# print(text.replace('еще', 'ЕЩЁ'))# позволяет поменять сочетание символов в нашей строке(первое какое хотим поментяь, второе на какое меняем)

m = 345
print(m*2)
print(int(m)*2)