N = int(input("Введите высоту пирамиды: "))
temp = -1
for i in range(N):
    temp = temp + 2
    print(" "*(N-1-i) + "*"*(temp))
