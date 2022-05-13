number = input('Введите число: ')
list_of_digit = list(str(number))
finding_digit = 5
if str(finding_digit) in list_of_digit:
    print('Цифра 5 есть в числе.')
else:
    print('Цифры 5 в числе нет.')
