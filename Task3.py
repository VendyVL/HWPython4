# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list1 = [10, 10, 23, 10, 17, 66, 45, 58, 17, 45]

def repit(list):
    res = []
    for i in range (0, len(list)):
        count = 0
        for j in range (0, len(list)):
            if list[i] == list[j]:
                count +=1
        res.append(count)
    list_res = []
    for i in range (0, len(list)):
        if res[i] == 1:
            list_res.append(list[i])
    return list_res

print(repit(list1))