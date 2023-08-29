# *** Типы данных ***

# целочисленные значения (int, integer)
my_int = 100

# числа с плавающей точкой (вещественные числа, дробные значения) (float)
my_float = 3.14

# булевы типы данных (bool, boolean) (логические типы данных)
# в честь Джорджа Буля (булева алгебра)
bool_1 = True # истина (логическая 1)
bool_2 = False # ложь (логический 0)

# строковые значения (символ, слово, текст) (str, string)
my_str_1 = 'A'
my_str_2 = "b"
my_str_3 = 'hello'
my_str_4 = "мой текст"
my_text = """
много
строчный
текст
"""

# print(my_text)

# Способы форматирования строк
# Конкатенация строк - старый способ 
str_1 = "Hello"
str_2 = "World"

num_1 = 777

res = str_1 + ' ' + str_2 + str(num_1)

# print(res)

# f-string (f-строка)
# res = f"Hello World {num_1}"
# res = f"Hello {str_2} {num_1}"

# print(res)

# Задание
# используя input("Ваше имя: ") вам неободимо сделать так,
# чтобы в ответ в терминале был такой результат:
# "Привет, Ольга!"

# name = input("Ваше имя: ")

# print(f"Привет, {name}!")

# Арифметические операции

a = 10
b = 3

# cложение
res = a + b

# вычитание
res = a - b

# умножение
res = a * b

# обычное деление
# всегда возвращает число с плавающей точкой
res = a / b

# целочисленное деление
res = a // b

# деление по остатку
res = a % b

print(res)