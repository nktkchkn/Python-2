# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а 
# Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а 
# Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


a = abs(int(input('Введите первое натуральное число a: ')))
b = abs(int(input('Введите второе натуральное число b: ')))

S = a + b   
P = a * b

b1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
a1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(a1, b1)