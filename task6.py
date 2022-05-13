numbers = int(input('Введите число: '))
suma = 0

while numbers > 0:
    digit = numbers % 10
    numbers = numbers // 10
    suma = suma + digit


print("Сумма цифр числа:", suma)