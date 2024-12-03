print('введите число') #выводим текст на поле
m = input() #считываем число
def is_even(n):
    if int(n) % 2 ==0:
        print('четное')
    else:
        print('нечетное')
is_even(m)