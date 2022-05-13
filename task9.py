number = int(input('Введите число: '))
a = number % 10
number = number//10
while number > 0:
    if number % 10 > a:
        a = number % 10
    number = number//10
print('Максимальная цифра в числе:', a)