string = input('Введите строку: ')
s = string.split()
n = k = maxlen = maxindex = int('0')

while k < len(s):
    if len(s[k]) > maxlen:
        maxlen = len(s[k])
        maxindex = k
    if len(s[k]) % 2 == 0:
        n = n + 1
    k = k + 1

print('Количество четных строк: ', n)
print('Самое длинное слово:', s[maxindex])