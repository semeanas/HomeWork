num = int(input("Введите натуральное число: "))
s = 0
while True:
    while num > 0:
        s = s + num % 10
        num = num // 10
    if s > 9:
        num = s
        s = 0
    else:
        break

print(s)
