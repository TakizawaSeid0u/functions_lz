print('введите число') #выводим текст на поле
m = input() #считываем число
v = int(0)
def temperature(n, c):
    c = (int(n)-32)*5/9
    return(c)
print(temperature(m, v))