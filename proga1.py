a = int(input('Введите число'))
k = int('1')
while k <= a//2:
    if a % k == 0:
        print(k)
    k = k + 1
print(a)
