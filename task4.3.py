# 3 Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {list}")
new_list = []
[new_list.append(i) for i in list if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")