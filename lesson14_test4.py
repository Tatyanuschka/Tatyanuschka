
def number_result(a):
    if a == 13:
        raise Exception('ValueError')
    else:
        return a ** 2
number = int(input('Введите число: '))
try:
    print(f' Квадрат числа равен: {number_result(number)}')
except:
    print('Было введено исключительное число 13')
