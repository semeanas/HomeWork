def alg (a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        temp = a % b
        a = temp
    if b > a:
        temp = b % a
        b = temp
    return alg(a, b)

a, b = int(input()), int(input())
x = alg(a, b)
print(x)
