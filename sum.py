def sums(nint, n, s):
    s += sum(nint)
    return(str(nint))


print('введите числа') #выводим текст на поле
v = (input()) #считываем строку
m = v.split() #разделяем по пробелу
nint = [0]
for i in m:
    nint.append(int(i))
sumOE = 0
print(sum(nint, sumOE))