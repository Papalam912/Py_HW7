# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 

# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху) 
# Если ритм есть, функция возвращает True, иначе возвращает False

# 	Примеры/Тесты:
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True


# vowel_letters = set("параплан")

# def count_Puh_rithm(sentence, isfullinf=False):
#     counters = set()
#     fullinf = []
#     for idx, phrase in enumerate(sentence.split()):
#         vowel_letters_count = 0
#         fullinf.append({})
#         for letter in phrase:
#             if letter in vowel_letters:
#                 vowel_letters_count += 1
#                 if letter in fullinf[idx]:
#                     fullinf[idx][letter] += 1
#                 else:
#                     fullinf[idx][letter] = 1
#         counters.add(vowel_letters_count)
#         if len(counters) != 1:
#             if isfullinf:
#                 return False, fullinf
#             else:
#                 return False
#     if isfullinf:
#         return True, fullinf
#     else:
#         return True

# print(count_Puh_rithm("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
# print(count_Puh_rithm("пара-ра-рам рам-пум-пупам па-ре-по-дам", True))
# print(count_Puh_rithm("пара-ра-рам рам-пуум-пупам па-ре-по-дам", True))

# print(count_Puh_rithm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па", True))
# print(count_Puh_rithm("Пам-парам-пурум Пум-пурум-карам", True))

# 6.2[32]: Напишите функцию ```print_operation_table(operation, num_rows=6, num_columns=6)```, которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы ```num_rows``` и ```num_columns``` указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
	
# 	Примеры/Тесты:
#     print_operation_table(lambda x,y: x**y,4,4)
# 	1   1   1   1
# 	2   4   8  16
# 	3   9  27  81
# 	4  16  64 256

#     print_operation_table(lambda x,y: x*y)
# 	1   2   3   4   5   6
# 	2   4   6   8  10  12
# 	3   6   9  12  15  18
# 	4   8  12  16  20  24
# 	5  10  15  20  25  30
# 	6  12  18  24  30  36

# def table(operation, num_rows=6, num_columns=6 ):
#     header = " "*7
#     for col in range(1, num_columns+1):
#         header +=f"{col:4d}"
#     print(header)
#     print(" "*7, "-"*num_columns*4)
#     for row in range(1, num_rows+1):
#         row_str = f"{row:4d} | "

#         for col in range(1, num_columns+1):
#             row_str += f"{operation(row, col):4d}"

#         print(row_str)

# table(lambda x,y: x*y)