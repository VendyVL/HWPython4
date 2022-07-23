# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

a = "63*x^3 + 56*x^2 + 4*x^1 + 59 = 0"
b = "4*x^5 + 50*x^4 + 38*x^3 + 5*x^2 + 1*x^1 + 58 = 0"

# Файлы попадают за пределы папки, которая идёт на гитхаб, а тут не слишком много данных, чтобы морочиться с этим.

list1 = a.split(" + ")
list2 = b.split(" + ")

def up(list):
    res = []
    a = len(list)
    while a!=0:
        res.append(list[a-1])
        a = a - 1
    return res

if len(list1) > len(list2): 
    first = up(list1)
    second = up(list2)
else:
    first = up(list2)
    second = up(list1)

def summ(list1,list2):
    k = len(list1) - len(list2)
    f = 1
    a = list1[0].split()
    b = list2[0].split()
    res = []
    res.append(f"{int(a[0])+int(b[0])} = 0")
    for i in range (1, len(list2)):
        c = list1[i].split("*")
        d = list2[i].split("*")
        res.append(f"{int(c[0])+int(c[0])}*x^{f}")
        f += 1
    for i in range (len(list2), len(list1)):
        res.append(list1[i])
    return res


print(" + " .join(up(summ(first,second))))