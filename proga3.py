spisok = [int(i) for i in input('Введите значения элементов через пробел ').split()]
k = 0
maxEl = spisok[0]
while k < len(spisok):
    if maxEl < spisok[k] and spisok[k] % 2 == 0:
        maxEl = spisok[k]
    k = k + 1
print(maxEl)
spisok.sort(reverse=True)
print(spisok)

