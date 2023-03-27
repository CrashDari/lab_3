# Страны Европы
name_to_number = [
    [1, 'Германия'], [2, 'Польша'], [3, 'Чехия'], [4, 'Австрия'], [5, 'Италия'], [6, 'Франция'],
    [7, 'Бельгия'], [8, 'Нидерланды'], [9, 'Великобритания'], [10, 'Дания'], [11, 'Норвегия'],
    [12, 'Швеция'], [13, 'Финляндия'],  [14, 'Литва'], [15, 'Латвия'], [16, 'Словакия'], [17, 'Венгрия'],
    [18, 'Хорватия'], [19, 'Греция'], [20, 'Испания']
]

distance = [
    [ float('inf'), 574, 345, 632, float('inf'), 1056, 756, 655, float('inf'), 438, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ 574, float('inf'), 637, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 523, 681, 662, float('inf'), float('inf'), float('inf'), float('inf')],
    [ 345, 637, float('inf'), 333, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 328, float('inf'), float('inf'), float('inf'), float('inf')],
    [ 632, float('inf'), 333, float('inf'), 1081, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 80, 243, float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), 1081, float('inf'), 1423, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1272, float('inf')],
    [ 1056, float('inf'), float('inf'), float('inf'), 1423, float('inf'), 312, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1275],
    [ 756, float('inf'), float('inf'), float('inf'), float('inf'), 312, float('inf'), 210, 377, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ 655, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 210, float('inf'), 421, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 377, 421, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ 438, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 654, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 522, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 654, 522, float('inf'), 544, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 544, float('inf'), float('inf'), 396, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ float('inf'), 523, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 295, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ float('inf'), 681, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 396, 295, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [ float('inf'), 662, 328, 80, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 200, float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), 243, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 200, float('inf'), 343, 1471, float('inf')],
    [ float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 343, float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), float('inf'), 1272, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1471, float('inf'), float('inf'), float('inf')],
    [ float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1275, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
]

orient_Europe = [
    [0 for i in range(20)] for j in range(20)
]

