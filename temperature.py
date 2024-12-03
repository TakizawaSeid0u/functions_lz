print('введите число') #выводим текст на поле
m = input() #считываем число
v = int(0)
def temperature(n, c):
    c = (float(n)*9/5)+32
    return(c)
print("температура по Фаренгейту", temperature(m, v))