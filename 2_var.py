# Однострочный комментарий

#  "Ctrl+/" - сочетание клавиш для однострочного комментария

# a = 100
# b = 200
# c = 300

'''многострочный
комментарий'''

"""
это тоже 
многострочный 
комментарий
"""

# *** Переменные ***

# snake_case (змеиная_нотация или стиль)
val_1 = 10
num_apples = 100

# camelCase (верблюжаяНотация след слово начинается с загл буквы и слитно)
myNumVar = 20

# константные переменные (константы)
CONST_VAR = 1000

# вызов встроенной функции вывода в терминал 
# print(val_1)
# print(myNumVar, CONST_VAR)


# встроенная функция ввода из терминала
# in_1 = input("Введите число: ")

# print(in_1)

# небольшой калькулятор
in_1 = input("Введите 1 число: ")
in_2 = input("Введите 2 число: ")

# конкатенация строк
# result = in_1 + in_2

# сложение чисел (после конвертации данных)
result = int(in_1) + int(in_2)

print(result)