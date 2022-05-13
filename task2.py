line = 10
count = 0

print('Введите 10 произвольных чисел.')

for number in range(1,line+1):
    m = int(input("Число " + str(number) + ": "))
    while m > 0:
        if m%10 == 5:
            count += 1
        m = m // 10

print(f'Итого 5-ок: {count} шт.')