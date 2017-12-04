def calc_multi (eq1,eq2):
    list1 = eq1
    list2 = eq2
    size1 = len(list1)
    size2 = len(list2)
    result = list()
    for i in range(0,size1):
        for j in range(0,size2):
            a = list1[i][0] * list2[j][0]
            b = list1[i][1]
            c = list1[i][2] + list2[j][2]
            d = list1[i][3]
            e = list1[i][4] + list2[j][4]
            result.append((a, b, c, d, e))
    return result
x= [(5, 'x', 10, 'y', 10), (9, 'x', 10, 'y', 40)]
y = [(5, 'x', 10, 'y', 10)]
print(calc_multi(x,y))

