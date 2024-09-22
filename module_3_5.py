#LIFO - last in first out
#Stack - принцип пирамидки

# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
# print(summa(5)) # n = 5 4 3 2 1 0, результат 0+1+2+3+4+5



# stack = []
# stack.append(1)
# print('Добавили элемент', stack)
# stack.append(2)
# print('Добавили элемент', stack)
# stack.append(3)
# print('Добавили элемент', stack)
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)


#Пример ошибки, где-то не вышли из ф-ии
# def recursion():
#     recursion()
# recursion()


# Напишите функцию get_multiplied_digits и параметр number в ней.
# Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять срез str_number[1:].
# Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.

#Пример
# def get_multiplied_digits(number):  # 1
#     number = int(number)            # отсекаем нули в начале number
#     str_number = str(number)        # 2
#     first = int(str_number[0])      # 3
#
#     while str_number.endswith('0'): # отсекаем нули в конце number
#             str_number = str_number[:len(str_number)-1]
#     if len(str_number) > 1:
#         return first * get_multiplied_digits(int(str_number[1:]))
#     else:
#         return first
#
# num = input('Введите целое число: ')
# print(f'Произведение цифр числа {num} :', get_multiplied_digits(num))

#Мое решение
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if str_number.endswith('0'):
        str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result = get_multiplied_digits(40200)
print(result)




















