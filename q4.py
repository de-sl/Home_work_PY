def pow_two():
    '''Эта функция возвращает целые степени двойки от 1 го до введенного числа'''
    try:
        n = int(input('Введите число:  '))
        num = []
        num1 = []
        lst =[2**i for i in range(1,n)]
        num1 = [2**i for i in range(1,n) if 2**i < n]
        if  len(num) != 0 and len(num1) !=0:
            return f' Целые степени двойки от одного до введенного числа это  - {num},Целые степени двойки от одного до введенного числа не превосходящие это число это {num1}'
        elif  len(num) != 0 and len(num1) ==0:
            return f' Целые степени двойки от одного до введенного числа это  - {num},Целые степени двойки от одного до введенного числа не превосходящие это число это отсутствуют'
        elif len(num) == 0:
            return 'Целые степени двойки от одного до вашего числа отсутствуют'
            
    except ValueError:
        return 'Вы ввели не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"
print(pow_two())