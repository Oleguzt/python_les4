# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без 
# повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 
# 1 строка - первый список через пробел. 
# 2 строка - второй список через пробел. 

list_1 = set(map(int, input().split()))
list_2 = set(map(int, input().split()))
print(sorted((list_1.intersection(list_2))))