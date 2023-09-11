import random

def coin():
    '''Эта функция, показывает какие монетки быстрее перевернуть'''
    try:
        my_lst = ["Орел","Решка"]
        lst = []
        n = int(input('Сколько раз вы хотите бросить монетку, введите число:   '))
        for _ in range(n+1):
            lst.append(random.choice(my_lst))
        if lst.count("Орел") < lst.count("Решка"):
            return f' Монеток, выпавших орлом меньше, нужно перевернуть {lst.count("Орел")}'
        if  lst.count("Решка") < lst.count("Орел"):
            return f' Монеток, выпавших решкой меньше, нужно перевернуть {lst.count("Решка")}'
        if lst.count("Орел") == lst.count("Решка"):
            return f'Выпало одинаковое количество орла и решки, вы можете перевернуть {lst.count("Решка")} любых монет'

    except ValueError:
        return 'Введено не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"
print(coin())