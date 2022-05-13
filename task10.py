count = 0

for number in range(1):
    number = int(input("Введите произвольное число: "))
    while number > 0:
        if number % 10 == 5:
            count += 1
        number = number // 10

print(f'Итого в числе 5-ок: {count} шт.')