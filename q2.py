import random

def watermelon_for_tescha():
    '''Эта функция решает впрос с арбузом'''
    try:
        lst = []
        n = int(input('Ведите количество арбузов в магазине: '))
        for _ in range(n+1):
            lst.append(random.randint(1,100))
        return f"Самый легкий арбуз весит {min(lst)} кг а самый большой {max(lst)}"
    except ValueError:
        return 'Вы ввели не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"
print(watermelon_for_tescha())