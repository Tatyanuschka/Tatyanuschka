fruits_1 = ['Яблоко', 'Груша', 'Апельсин', 'Лимон', 'Банан', 'Ананас', 'Виноград']
fruits_2 = ['Апельсин', 'Киви', 'Грейпфрут', 'Груша', 'Манго', 'Ананас', 'Арбуз']
# классическое решение
# result = []
# for i in range (len(fruits_1)-1):
#     for y in range (len(fruits_2)-1):
#        if fruits_2[y] == fruits_1[i]:
#            result.append(fruits_2[y])
# print(result)
fruits_3 = [fruit for fruit in fruits_2 if fruit == fruit in fruits_1]
print(fruits_3)
