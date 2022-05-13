numbers = int(input('Введите число: '))
mult = 1

while numbers > 0:
    digit = numbers % 10
    numbers = numbers // 10
    mult = mult * digit

print("Произведение цифр числа:", mult)