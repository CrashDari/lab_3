#начальные данные(цикл для ввода)
coins = []
n = int(input('введите сумму, которую нужно получить из монет:  '))
print('монеты: ')
for i in range(4):
    coins.append([int(input('ценность монеты:  ')),int(input('количество монет:  '))])

def coin_master(coin_array, n):
    coin_combinations = []
    total = 0 # считаем подходящую сумму монет
    coin_array.sort(reverse = True) #сортируем массив в порядке убывания
    for coin in coin_array:
        num = coin[1] # количество монет
        c = coin[0] # ценность монеты
        while total != n and num >0:
# пока есть монетки и их сумма подходит, то добавляем её в нашу комбинацию
            if total + c <= n:
                total+=c
                coin_combinations.append(c)
                num-=1
            else:
                break
    if total != n: # если комбинацию составить невозможно, товыводим сообщение об ошибке
        print('невозможно составить комбинацию')
    else:
        print(coin_combinations,total)
coin_master(coins, n)
    
