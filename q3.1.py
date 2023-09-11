def solver():
        a = int(input('Введите сумму чисел  '))
        b = int(input('Введите произведение чисел  '))
        x = (a-int((a**2-4*b)**0.5))//2
        y = (a+int((a**2-4*b)**0.5))//2
        print(f'Ваши числа {x} и {y}')
    
solver()

