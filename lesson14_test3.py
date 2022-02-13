import random
import math

def result_list(list_in):
    list_out = [round(math.sqrt(number), 2) if number >= 0 else number for number in list_in]
    return list_out
old_list = [random.randint(-20, 20) for i in range (20)]
print(f'Исходный список: {old_list}')
print(f'Итоговый список: {result_list(old_list)}')



