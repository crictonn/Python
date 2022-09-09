goods = {'Кольцо': ['Золото', 99, 56],
         'Подеска': ['Золото', 150, 40],
         'Серьги': ['Серебро', 49, 75],
         'Браслет': ['Палладий', 100, 20]
         }
def show_descr(k):
    name = input('Введите название: ').capitalize()
    if name in goods:
        if k == 1:
            print('Описание:\n \tМатериал:', goods[name][0],'\tЦена:', goods[name][1])
        if k == 2:
            print('Цена на "', name, '" равна: ', goods[name][1], ' рублей ')
        if k == 3:
            print('Сейчас в магазине: ', goods[name][2])

def purchase():
    name = input('Введите название: ').capitalize()
    if name in goods:
        amount = int(input('Введите количество: '))
        print('Вы собираетесь купить ', amount, ' ',name, ' на сумму ', goods[name][1] * amount)
        agree = int(input('Продолжить?\n1. Да\n2. Нет\n'))
        if agree == 1:
            goods[name][2] = goods[name][2] - amount
            print('Покупка совершена!')
        # elif agree == 2:
        #     break

def selection():

    pass
    print('1. Просмотр описания\n' 
      '2. Просмотр цены\n' 
      '3. Просмотр количества\n'
      '4. Вся информация\n'
      '5. Покупка\n'
      '6. Выход')

while 1:
    selection()
    k = int(input('Выбор: '))
    if k <= 3:
        show_descr(k)
    elif k == 4:
        for i in goods:
            print('Наименование: "', i, '", материал: ', goods[i][0], ' цена: ', goods[i][1], ' количество в магазине: ', goods[i][2])
    elif k == 5:
        purchase()
    elif k == 6:
        break
