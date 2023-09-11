def guess_numbers():
    '''Эта функция находит 2 загаданных числа'''
    try:
        num1 = int(input('Ведите первое число от 1 го до 1000  '))
        num2 = int(input("Введите второе число от 1 го до 1000  "))
        p =  int(input('Ведите произведение ваших чисел   '))
        s =  int(input("Введите сумму ваших чисел   "))
        if 1<= num1 <= 1000 and 1<=num2 <= 1000 and num1 + num2 == s and num1 * num2 == p: 
            for num1 in range(1, min(s, p) + 1):
                num2 = s - num1
                if num1 * num2 == p:
                    return f'Вы загадали числа {num1}  и {num1}'
                
        else:
            return f'Ваши числа не подходят под условие'
    except ValueError:
        return 'Вы ввели не число'
    except KeyboardInterrupt:
        return "Ведены не все данные"
print(guess_numbers())